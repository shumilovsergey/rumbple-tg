from .telegram_def import auth
from .telegram_def import message_send
from .keyboards import menu_button
import telebot
from project.const import TOKEN
bot = telebot.TeleBot(TOKEN)

def routers_audio(message):
    if auth(message.chat.id):
        bot.send_message(
            text=(message.json["audio"]["file_id"]) + "\n" + (message.json["audio"]["file_name"]),
            chat_id=message.chat.id
        )
    else:
        bot.delete_message(message.chat.id, message.message_id)
    return