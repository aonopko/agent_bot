from aiogram.dispatcher import FSMContext
from asyncpg.exceptions import UniqueViolationError, DataError
from aiogram import types
from aiogram.dispatcher.filters import Command
from keybords.reply_keybords import menu
from create_bot import dp, db, bot
from states import Route


@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer('Привіт агент', reply_markup=menu)


@dp.message_handler(text="Додати агента")
async def new_agent(message: types.Message):
    try:
        await db.add_agent(
            full_name=message.from_user.full_name,
            telegram_id=message.from_user.id)
    except UniqueViolationError:
        await bot.send_message(message.from_user.id,
                               f"Agent {message.from_user.id} існує")
    else:
        await message.reply('Агента додано')


@dp.message_handler(text="Додати маршрут")
async def enter_route(message: types.Message):
    await message.answer("Додайте початкові дані")

    await Route.initial_readings.set()


@dp.message_handler(state=Route.initial_readings)
async def answer_initial_readings(message: types.Message,
                                  state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        try:
            data["initial_readings"] = int(answer)
        except ValueError:
            await message.reply("Потрібно ввести число")

        else:
            await bot.send_message(message.from_user.id, "Додайте кінцеві дані")
            await Route.next()


@dp.message_handler(state=Route.final_readings)
async def answer_final_readings(message: types.Message,
                                state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        try:
            data["final_readings"] = int(answer)
        except ValueError:
            await message.reply("Потрібно ввести число")
        else:
            await bot.send_message(message.from_user.id, "Додано кінцеві дані")
            await Route.next()
            await state.finish()

    initial_readings = data.get("initial_readings")
    final_readings = data.get("final_readings")
    difference_readings = int(final_readings) - int(initial_readings)
    try:
        await db.add_route(initial_readings=initial_readings,
                           final_readings=final_readings,
                           id_agent=message.from_user.id,
                           difference_readings=difference_readings)
    except DataError:
        await bot.send_message(message.from_user.id, "Помилка")

    await message.answer("Дані маршруту додано")

