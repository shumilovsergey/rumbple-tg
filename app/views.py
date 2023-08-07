import re
import json
from django.contrib import admin
from .models import Chats
from .models import Moderators
from .models import Janras
from .models import Files
from .models import Artists
import requests
from project.const import TOKEN
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import telebot
from telebot.types import Update




MENU_BUTTON = {
        "inline_keyboard" :  [
            [
                {'text': 'Меню', 'callback_data': 'menu/'}
            ]
        ]
    }

MAIN_MENU = {
    "inline_keyboard" :  [
        [
            {'text': 'Прослушать историю', 'callback_data': 'menu_play/'}
        ],
        [
            {'text': 'Записать историю', 'callback_data': 'menu_record/'}
        ]
    ]
}




bot = telebot.TeleBot(TOKEN)
@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        update = update_parser(request)
        format = format_message(update)

        if format == "callback":
            callback_query = update.callback_query
            chat_id = callback_query.from_user.id
        else:
            message = update.message
            chat_id = message.chat.id
            
#############################################################
        if format == "text":
            if message.text == "/start":
                rout_start(message)

            elif message.text == "/chat_id":
                rout_chat_id(message)

            elif message.text == "/add":   #MODERATOR
                rout_add(message)



        elif format == "audio":   #MODERATOR
            print("rout audio")
            # rout_audio(message)
        
        elif format == "callback":
            pass
            # if callback_text(callback_query) == "menu_add/":
            #     callback_menu_add(callback_query)
 
        
    return JsonResponse({'status': 'ok'})


#############################################################

def rout_start(message):
    chat_id = message.chat.id
    message_id = message.message_id

    new_chat = Chats(
        chat_id=chat_id,
        last_callback = "none/",
        last_id = "none/"
    )
    new_chat.save()

    text = " Главное  Меню "
    keyboard = MAIN_MENU
    message_send(text=text, keyboard=keyboard, chat_id=chat_id)
    return

def rout_chat_id(message):
    chat_id = message.chat.id
    message_id = message.message_id

    text = f"Ваш телеграм id: {chat_id}"
    keyboard = MENU_BUTTON
    message_send(text=text, keyboard=keyboard, chat_id=chat_id)
    bot.delete_message(chat_id, message_id)
    return

def rout_add(message):
    chat_id = message.chat.id
    message_id = message.message_id

    if auth(chat_id):
        if Janras.objects.count() > 0:
            text = "Какой жанр истории хотите загрузить?"
            group_number = "1"
            keyboard = keyboard_add(group_number)
            message_send(chat_id=chat_id, keyboard=keyboard, text=text)
        
        else:
            text = "Жанры историй еще не добавлены"
            bot.send_message(chat_id, text)

    bot.delete_message(chat_id, message_id)
    return

#############################################################
def callback_menu_add(callback_query):
    janra_id = callback_number(callback_query)
    message_id = callback_query.message.message_id
    chat_id = callback_query.message.chat.id
    callback = callback_query.data

    # bot.delete_message(chat_id, message_id)
    try:
        janra = Janras.objects.get(id=janra_id)
        user = Chats.objects.get(chat_id=chat_id)
        user.last_callback = callback
        user.last_id = chat_id
        user.save()

        text = "Отлично! Теперь отправьте мне озвученную историю!"
    except:
        text = "Ошибка! Жанр был удален, попробуйте еще раз ввести команду /add"
    bot.edit_message_text(text=text, chat_id=chat_id, message_id=message_id)
    return

def callback_menu(callback_query):
    message_id = callback_query.message.message_id
    chat_id = callback_query.message.chat.id
    text = "Главное  Меню"
    keyboard = MAIN_MENU
    message_send(chat_id=chat_id, text=text, keyboard=keyboard)
    bot.delete_message(chat_id, message_id)

def callback_menu_play(callback_query):
    message_id = callback_query.message.message_id
    chat_id = callback_query.message.chat.id

    if Janras.objects.count() > 0:
        text = "Какой жанр истории хотите послушать?"
        group_number = "1"
        keyboard = keyboard_get(group_number)
        message_send(chat_id=chat_id, keyboard=keyboard, text=text)
    
    else:
        text = "Жанров еще нет :("
        message_send(chat_id=chat_id, text=text, keyboard=MENU_BUTTON)

    bot.delete_message(chat_id, message_id)
    return

def callback_menu_get_group_up(callback_query):
    message_id = callback_query.message.message_id
    chat_id = callback_query.message.chat.id
    group_number = callback_number(callback_query)
    keyboard = keyboard_get(group_number)
    text = "Какой жанр истории хотите выбрать?"
    message_edit(chat_id=chat_id, text=text, keyboard=keyboard, message_id=message_id)
    return

def callback_menu_add_group_up(callback_query):
    message_id = callback_query.message.message_id
    chat_id = callback_query.message.chat.id
    group_number = int(callback_number(callback_query))
    keyboard = keyboard_add(group_number)
    text = "Какой жанр истории хотите загрузить?"
    message_edit(chat_id=chat_id, text=text, keyboard=keyboard, message_id=message_id)
    return

#############################################################
def update_parser(request):
    json_str = request.body.decode('UTF-8')
    update = Update.de_json(json_str)
    print(update)
    return update

def format_message(update):

    status = True
    type_message = "None"

    if status:
        if str(update.callback_query) != "None" and status:
            type_message = "callback"
            status = False 
    if status:
        if str(update.message.content_type) == "text":
            type_message = "text"
            status = False

    if status:
        if str(update.message.content_type) == "voice":
            type_message = "voice"
            status = False
    if status:
        if str(update.message.content_type) == "photo":
            type_message = "photo"
            status = False
    if status:
        if str(update.message.content_type) == "audio":
            type_message = "audio"
            status = False
    if status:
        if str(update.message.content_type) == "video_note":
            type_message = "video_note"
            status = False
    if status:
        if str(update.message.content_type) == "video":
            type_message = "video"
            status = False
    if status:
        if str(update.message.content_type) == "document":
            type_message = "document"
            status = False

 
    print(type_message)###<<<###
    return type_message

def callback_text(callback_query):
    callback = callback_query.data
    string = callback.split("/")
    text = string[0] + "/"
    return text

def callback_number(callback_query):
    numbers_list = re.findall(r'\d+', callback_query.data)
    number = ''.join(numbers_list)
    return number   


def auth(chat_id):
    status = False
    try:
        moderator = Moderators.objects.get(chat_id=chat_id)
        status = True
    except:
        pass
    return status    

#######################
def message_send(chat_id, text, keyboard):
    data = { 
        "chat_id": chat_id,
        "text": text,
        "reply_markup" : json.dumps(keyboard)
    }
    response = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data)
    return response

def audio_send(chat_id, text, keyboard, audio_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'
    data = {
        'chat_id': chat_id, 
        'caption': text, 
        'audio': audio_id,
        "reply_markup" : json.dumps(keyboard)
    }

    response = requests.post(url, data=data)
    return response

def message_edit(chat_id, message_id, text, keyboard):
    data = { 
        "chat_id": chat_id,
        "text": text,
        "message_id" : message_id,
        "reply_markup" : json.dumps(keyboard)
    }
    response = requests.post(f"https://api.telegram.org/bot{TOKEN}/editMessageText", data)
    return response