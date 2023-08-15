
from .models import Chats
from .keyboards import main_menu
from .keyboards import menu_button
from .telegram_def import message_send
from .telegram_def import auth
from project.const import TOKEN
from .telegram_def import json_dict




def routers_text(message):
    message=json_dict(message)

    if message.text == "/start":
        rout_start(message)


    elif message.text == "/chat_id":
        rout_chat_id(message)

    elif message.text == "/add":   #MODERATOR
        rout_add(message)


#############################################

def rout_start(message):
    user = message.user_info
    if "username" in user:
        user_name = user["username"]
    else:
        user_name = "None"

    if "last_name" in user:
        last_name = user["last_name"]
    else:
        last_name = "None"

    if "first_name" in user:
        first_name = user["first_name"]
    else:
        first_name = "None"

    new_chat = Chats(   
        chat_id= message.chat_id,
        first_name= first_name,
        last_name= last_name,
        user_name= user_name
    )
    new_chat.save()

    text = " Главное  Меню "    
    keyboard = main_menu()
    message_send(text=text, keyboard=keyboard, chat_id=message.chat_id)
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