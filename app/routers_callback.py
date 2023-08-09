from .telegram_def import callback_json
from .keyboards import main_menu
from .keyboards import menu_button
from .telegram_def import message_send
from .telegram_def import message_edit
import telebot
from project.const import TOKEN
bot = telebot.TeleBot(TOKEN)

def routers_callback(callback_query):
    data = callback_json(callback_query)
    callback = {
        "chat_id": callback_query.message.chat.id,
        "message_id": callback_query.message.message_id,
        "data": data
    }

    if data.get("menu") == "menu":
        menu(callback)

    if data.get("info") == "info":
        info(callback) 

    if data.get("sql") == "get" and data.get("janra") == "?":
        janra_menu(callback) 
###

def menu(callback):
    message_edit(
        text= "Главное  Меню",
        message_id= callback.get("message_id"),
        chat_id= callback.get("chat_id"),
        keyboard= main_menu()
    )
    return

def info(callback):
    message_edit(
        text= "Тут могут быть всякие полезные ссылки",
        message_id= callback.get("message_id"),
        chat_id= callback.get("chat_id"),
        keyboard= menu_button()
    )
    return

def janra_menu(callback):

    return