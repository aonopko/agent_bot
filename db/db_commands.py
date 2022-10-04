from telegrambot.users.models import User

from asgiref.sync import sync_to_async


@sync_to_async
def select_user(telegram_id: int):
    user = User.object.filter(telegram_id=telegram_id).first()
    return user


@sync_to_async
def add_user(user_name, telegram_id):
    try:
        return User(user_name=user_name, telegram_id=telegram_id).save()
    except Exception:
        return User.user_name
