from .telegram_def import callback_json
from .keyboards import main_menu
from .keyboards import menu_button
from .keyboards import sql_keyboard
from .telegram_def import message_edit
from .telegram_def import message_send
from .telegram_def import message_delete
from .telegram_def import audio_send
from .models import Janras
from .models import Files
from .models import Artists
from .models import VideoJanras
from .models import VideoFiles
from .models import VideoArtists

import json

def routers_callback(message):
    callback = callback_json(message["callback"])
    message["callback"] = callback

    if message["callback"].get("menu") == "menu":
        menu(message)

    elif message["callback"].get("info") == "info":
        info(message) 
#AUDIO
    elif message["callback"].get("a_janra") == "?":
        audio_janra_menu(message) 

    elif message["callback"].get("a_artist") == "?":
        audio_artist_menu(message) 

    elif message["callback"].get("a_file") == "?":
        audio_file_menu(message) 

    elif message["callback"].get("a_file_get") == "?":
        audio_file_get(message)
#VIDEO
    elif message["callback"].get("v_janra") == "?":
        video_janra_menu(message) 

    elif message["callback"].get("v_artist") == "?":
        video_artist_menu(message) 

    elif message["callback"].get("v_file") == "?":
        video_file_menu(message) 

    elif message["callback"].get("v_file_get") == "?":
        video_file_get(message)
###

def menu(message):
    message_edit(
        text= "Главное  Меню",
        message_id= message["message_id"],
        chat_id= message["chat_id"],
        keyboard= main_menu()
    )
    return

def info(message):
    message_edit(
        text= "Тут могут быть всякие полезные ссылки",
        message_id= message["message_id"],
        chat_id= message["chat_id"],
        keyboard= menu_button()
    )
    return

#AUDIO
def audio_janra_menu(message):
    next_key = "a_artist" #HARDKODING! 

    method = message["callback"]["sql"]
    group = int(message["callback"]["g"])
    
    all_elements = Janras.objects.all()
    element_count = int(len(all_elements))
    amount = element_count - ( 6*group )


    if group > 1:
        back_button = {
            "sql": method,
            "g": str(group-1),
            "a_janra": "?"
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
            "a_janra": "?"
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
        message_id= message["message_id"],
        chat_id= message["chat_id"],
        keyboard= sql_keyboard(**kwargs)
    )
    return

def audio_artist_menu(message):
    next_key = "a_file" #HARDKODING! 

    method = message["callback"]["sql"]
    group = int(message["callback"]["g"])
    filter = message["callback"]["f"]
    
    janra = Janras.objects.get(id=filter)
    all_elements = Artists.objects.filter(janra=janra)

    element_count = int(len(all_elements))
    amount = element_count - ( 6*group )


    if group > 1:
        back_button = {
            "sql": method,
            "g": str(group-1),
            "a_artist": "?", #HARDKODING! 
            "f": filter
        }
    else:
        back_button = {    #HARDKODING! 
            "sql":"get",
            "g":"1",
            "a_janra":"?",
            "f":"-"
        }


    navigation= [
        {'text': "◀", 'callback_data': json.dumps(back_button)} 
    ]     

    if amount > 0:
        next_button= {
            "sql": method,
            "g": str(group+1),
            "a_artist": "?",
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
        text= "Жанр - " + janra.name,
        message_id= message["message_id"],
        chat_id= message["chat_id"],
        keyboard= sql_keyboard(**kwargs)
    )
    return

def audio_file_menu(message):
    next_key = "a_file_get" #HARDKODING! 

    method = message["callback"]["sql"]
    group = int(message["callback"]["g"])
    filter = message["callback"]["f"]
    
    artist = Artists.objects.get(id=filter)
    all_elements = Files.objects.filter(artist=artist)

    element_count = int(len(all_elements))
    amount = element_count - ( 6*group )

    artist = Artists.objects.get(id=filter)
    janra = artist.janra
    
    if group > 1:
        back_button = {
            "sql": method,
            "g": str(group-1),
            "a_file": "?", #HARDKODING! 
            "f": filter
        }
    else:
        back_button = {    #HARDKODING! 
            "sql":"get",
            "g":"1",
            "a_artist":"?",
            "f": janra.id
        }


    navigation= [
        {'text': "◀", 'callback_data': json.dumps(back_button)} 
    ]     

    if amount > 0:
        next_button= {
            "sql": method,
            "g": str(group+1),
            "a_file": "?",
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
        text= artist.name,
        message_id= message["message_id"],
        chat_id= message["chat_id"],
        keyboard= sql_keyboard(**kwargs)
    )
    return

def audio_file_get(message):
    message_delete(
        chat_id=message["chat_id"],
        message_id=message["message_id"]
    )

    file = Files.objects.get(id=message["callback"]["f"])
    audio_send(
        text ="",
        chat_id=message["chat_id"],
        audio_id=file.tg_id,
        keyboard={}

    )
    
    message_send(
        chat_id=message["chat_id"],
        text = " Главное  Меню ",
        keyboard=main_menu()
    )
    
    return

#VIDEO

def video_janra_menu(message):
    next_key = "v_artist" #HARDKODING! 

    method = message["callback"]["sql"]
    group = int(message["callback"]["g"])
    
    all_elements = VideoJanras.objects.all()
    element_count = int(len(all_elements))
    amount = element_count - ( 6*group )


    if group > 1:
        back_button = {
            "sql": method,
            "g": str(group-1),
            "v_janra": "?"
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
            "v_janra": "?"
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
        message_id= message["message_id"],
        chat_id= message["chat_id"],
        keyboard= sql_keyboard(**kwargs)
    )
    return

def video_artist_menu(message):
    next_key = "v_file" #HARDKODING! 

    method = message["callback"]["sql"]
    group = int(message["callback"]["g"])
    filter = message["callback"]["f"]
    
    janra = VideoJanras.objects.get(id=filter)
    all_elements = VideoArtists.objects.filter(janra=janra)

    element_count = int(len(all_elements))
    amount = element_count - ( 6*group )


    if group > 1:
        back_button = {
            "sql": method,
            "g": str(group-1),
            "v_artist": "?", #HARDKODING! 
            "f": filter
        }
    else:
        back_button = {    #HARDKODING! 
            "sql":"get",
            "g":"1",
            "v_janra":"?",
            "f":"-"
        }


    navigation= [
        {'text': "◀", 'callback_data': json.dumps(back_button)} 
    ]     

    if amount > 0:
        next_button= {
            "sql": method,
            "g": str(group+1),
            "v_artist": "?",
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
        text= "Жанр - " + janra.name,
        message_id= message["message_id"],
        chat_id= message["chat_id"],
        keyboard= sql_keyboard(**kwargs)
    )
    return

def video_file_menu(message):
    next_key = "v_file_get" #HARDKODING! 

    method = message["callback"]["sql"]
    group = int(message["callback"]["g"])
    filter = message["callback"]["f"]
    
    artist = VideoArtists.objects.get(id=filter)
    all_elements = VideoFiles.objects.filter(artist=artist)

    element_count = int(len(all_elements))
    amount = element_count - ( 6*group )

    artist = VideoArtists.objects.get(id=filter)
    janra = artist.janra
    
    if group > 1:
        back_button = {
            "sql": method,
            "g": str(group-1),
            "v_file": "?", #HARDKODING! 
            "f": filter
        }
    else:
        back_button = {    #HARDKODING! 
            "sql":"get",
            "g":"1",
            "v_artist":"?",
            "f": janra.id
        }


    navigation= [
        {'text': "◀", 'callback_data': json.dumps(back_button)} 
    ]     

    if amount > 0:
        next_button= {
            "sql": method,
            "g": str(group+1),
            "v_file": "?",
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
        text= artist.name,
        message_id= message["message_id"],
        chat_id= message["chat_id"],
        keyboard= sql_keyboard(**kwargs)
    )
    return

def video_file_get(message):
    message_delete(
        chat_id=message["chat_id"],
        message_id=message["message_id"]
    )

    file = VideoFiles.objects.get(id=message["callback"]["f"])
    audio_send(
        text ="",
        chat_id=message["chat_id"],
        audio_id=file.tg_id,
        keyboard={}

    )
    
    message_send(
        chat_id=message["chat_id"],
        text = " Главное  Меню ",
        keyboard=main_menu()
    )
    
    return