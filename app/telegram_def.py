import json
from .models import Moderators
import requests
from project.const import TOKEN
from telebot.types import Update


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

def auth(chat_id):
    status = False
    try:
        moderator = Moderators.objects.get(chat_id=chat_id)
        status = True
    except:
        pass
    return status    

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

def callback_json(callback_query):
    callback_json = False
    try:
        callback_json = json.loads(callback_query.data)  
    except:
        pass
    return callback_json





