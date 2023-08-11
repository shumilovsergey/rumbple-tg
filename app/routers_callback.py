from .telegram_def import callback_json
from .keyboards import main_menu
from .keyboards import menu_button
from .keyboards import sql_keyboard
from .telegram_def import message_edit
import telebot
from project.const import TOKEN
from .models import Janras
from .models import Files
from .models import Artists
bot = telebot.TeleBot(TOKEN)
import json

def routers_callback(callback_query):
    data = callback_json(callback_query)
    callback = {
        "chat_id": callback_query.message.chat.id,
        "message_id": callback_query.message.message_id,
        "data": data
    }

    if data.get("menu") == "menu":
        menu(callback)

    elif data.get("info") == "info":
        info(callback) 

    elif data.get("janra") == "?":
        janra_menu(callback) 

    elif data.get("artist") == "?":
        artist_menu(callback) 

    elif data.get("file") == "?":
        file_menu(callback) 

    elif data.get("file_get") == "?":
        file_get(callback)
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
    next_key = "artist" #HARDKODING! 

    method = callback["data"]["sql"]
    group = int(callback["data"]["g"])
    
    all_elements = Janras.objects.all()
    element_count = int(len(all_elements))
    amount = element_count - ( 6*group )


    if group > 1:
        back_button = {
            "sql": method,
            "g": str(group-1),
            "janra": "?"
        }
    else:
        back_button = {
            "menu":"menu"
        }

    navigation= [
        {'text': "◀", 'callback_data': json.dumps(back_button)} 
    ]     

    if amount > 0:
        next_button= {
            "sql": method,
            "g": str(group+1),
            "janra": "?"
        }
        navigation.append({'text': "▶", 'callback_data': json.dumps(next_button)})


    kwargs = {
        "group":group,
        "all_elements":all_elements,
        "next_key":next_key,
        "navigation":navigation,
        "method":method
    }
    message_edit(
        text= "Выбор жанра",
        message_id= callback.get("message_id"),
        chat_id= callback.get("chat_id"),
        keyboard= sql_keyboard(**kwargs)
    )
    return

def artist_menu(callback):
    next_key = "file" #HARDKODING! 

    method = callback["data"]["sql"]
    group = int(callback["data"]["g"])
    filter = callback["data"]["f"]
    
    janra = Janras.objects.get(id=filter)
    all_elements = Artists.objects.filter(janra=janra)

    element_count = int(len(all_elements))
    amount = element_count - ( 6*group )


    if group > 1:
        back_button = {
            "sql": method,
            "g": str(group-1),
            "artist": "?", #HARDKODING! 
            "f": filter
        }
    else:
        back_button = {    #HARDKODING! 
            "sql":"get",
            "g":"1",
            "janra":"?",
            "f":"-"
        }


    navigation= [
        {'text': "◀", 'callback_data': json.dumps(back_button)} 
    ]     

    if amount > 0:
        next_button= {
            "sql": method,
            "g": str(group+1),
            "artist": "?",
            "f":filter
        }
        navigation.append({'text': "▶", 'callback_data': json.dumps(next_button)})


    kwargs = {
        "group":group,
        "all_elements":all_elements,
        "next_key":next_key,
        "navigation":navigation,
        "method":method
    }
    message_edit(
        text= "Выбор исполнителя",
        message_id= callback.get("message_id"),
        chat_id= callback.get("chat_id"),
        keyboard= sql_keyboard(**kwargs)
    )
    return

def file_menu(callback):
    next_key = "file_get" #HARDKODING! 

    method = callback["data"]["sql"]
    group = int(callback["data"]["g"])
    filter = callback["data"]["f"]
    
    artist = Artists.objects.get(id=filter)
    all_elements = Files.objects.filter(artist=artist)

    element_count = int(len(all_elements))
    amount = element_count - ( 6*group )


    if group > 1:
        back_button = {
            "sql": method,
            "g": str(group-1),
            "file": "?", #HARDKODING! 
            "f": filter
        }
    else:
        back_button = {    #HARDKODING! 
            "sql":"get",
            "g":"1",
            "artist":"?",
            "f": filter
        }


    navigation= [
        {'text': "◀", 'callback_data': json.dumps(back_button)} 
    ]     

    if amount > 0:
        next_button= {
            "sql": method,
            "g": str(group+1),
            "file": "?",
            "f":filter
        }
        navigation.append({'text': "▶", 'callback_data': json.dumps(next_button)})


    kwargs = {
        "group":group,
        "all_elements":all_elements,
        "next_key":next_key,
        "navigation":navigation,
        "method":method
    }
    message_edit(
        text= "Выбор произведения",
        message_id= callback.get("message_id"),
        chat_id= callback.get("chat_id"),
        keyboard= sql_keyboard(**kwargs)
    )
    return

def file_get(callback):
    return