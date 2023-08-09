
from .models import Chats
from .keyboards import main_menu
from .keyboards import menu_button
from .telegram_def import message_send
from .telegram_def import auth
import telebot
from project.const import TOKEN
bot = telebot.TeleBot(TOKEN)


def routers_text(message):
    if message.text == "/start":
        rout_start(message)

    elif message.text == "/chat_id":
        rout_chat_id(message)

    elif message.text == "/add":   #MODERATOR
        rout_add(message)


#############################################

def rout_start(message):

    new_chat = Chats(   
        chat_id= message.chat.id,
        first_name= message.chat.first_name,
        last_name= message.chat.last_name,
        username= message.chat.username
    )
    new_chat.save()

    text = " Главное  Меню "    
    keyboard = main_menu()
    message_send(text=text, keyboard=keyboard, chat_id=message.chat.id)
    return

def rout_chat_id(message):
    chat_id = message.chat.id
    message_id = message.message_id

    text = f"Ваш телеграм id: {chat_id}"
    keyboard = menu_button()
    message_send(text=text, keyboard=keyboard, chat_id=chat_id)
    bot.delete_message(chat_id, message_id)
    return

def rout_add(message): 
    chat_id = message.chat.id
    message_id = message.message_id

    if auth(chat_id):
        pass
    bot.delete_message(chat_id, message_id)
    return