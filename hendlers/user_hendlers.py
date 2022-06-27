from aiogram.dispatcher import FSMContext
from asyncpg.exceptions import UniqueViolationError, DataError
from aiogram import types
from aiogram.dispatcher.filters import Command
from keybords.reply_keybords import menu
from create_bot import dp, db, bot
from states import Route


@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer('HI AGENT', reply_markup=menu)


@dp.message_handler(text="add agent")
async def new_agent(message: types.Message):
    try:
        await db.add_agent(
            full_name=message.from_user.full_name,
            telegram_id=message.from_user.id)
    except UniqueViolationError:
        await bot.send_message(message.from_user.id,
                               f"Agent {message.from_user.id} exists ")
    else:
        await message.reply('Agent is add')


@dp.message_handler(text="add route")
async def enter_route(message: types.Message):
    await message.answer("enter initial_readings")

    await Route.initial_readings.set()


@dp.message_handler(state=Route.initial_readings)
async def answer_initial_readings(message: types.Message,
                                  state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        try:
            data["initial_readings"] = int(answer)
        except ValueError:
            await message.reply("Enter integer")

        else:
            await bot.send_message(message.from_user.id, "Enter final_readings")
            await Route.next()


@dp.message_handler(state=Route.final_readings)
async def answer_final_readings(message: types.Message,
                                state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        try:
            data["final_readings"] = int(answer)
        except ValueError:
            await message.reply("Enter integer")
        else:
            await Route.next()
            await message.reply("Data is add")

    initial_readings = data.get("initial_readings")
    final_readings = data.get("final_readings")
    difference_readings = final_readings - initial_readings
    try:
        await db.add_route(initial_readings=initial_readings,
                           final_readings=final_readings,
                           id_agent=message.from_user.id,
                           difference_readings=difference_readings)
    except DataError:
        await bot.send_message(message.from_user.id, "Error")

    await message.answer("data is enter")
    await state.finish()
