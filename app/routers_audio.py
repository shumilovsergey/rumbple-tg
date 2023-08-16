from .telegram_def import auth
from .telegram_def import message_send
import telebot
from project.const import TOKEN
bot = telebot.TeleBot(TOKEN)

def routers_audio(message):

    if auth(message["chat_id"]):
        message_send(
            text= message["audio_id"] + "\n" + message["audio_name"],
            chat_id= message["chat_id"],
            keyboard={}
        )

    else:
        bot.delete_message(message["chat_id"], message["message_id"])

    return