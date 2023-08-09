from .telegram_def import is_it_sql
from .keyboards import main_menu
from .telegram_def import message_send
import telebot
from project.const import TOKEN
bot = telebot.TeleBot(TOKEN)

def routers_callback(callback_query):
    callback_json = is_it_sql(callback_query)
    if callback_json == False:
### ОБЫЧНЫЙ КОЛБЕК
        print(" обычный колбек ")
    else:
### SQL КОЛБЕК
        print(" скуэль колбек ")
                    
        if callback_query.data == "menu":
            callback_menu(callback_query)
 
###

def callback_menu(callback_query):
    message_id = callback_query.message.message_id
    chat_id = callback_query.message.chat.id
    text = "Главное  Меню"
    keyboard = main_menu()
    message_send(chat_id=chat_id, text=text, keyboard=keyboard)
    bot.delete_message(chat_id, message_id)
