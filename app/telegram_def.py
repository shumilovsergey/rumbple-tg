import json
from .models import Moderators
import requests
from project.const import TOKEN
from .models import Logs

class json_dict:
    def __init__(self, data):
        self.data = data   

    def __getattr__(self, item):
        return self.data.get(item, "none")

def format_message(request):
    message = {}
    data = json.loads(request.body.decode('utf-8'))
    report = False

    if "message" in data:
        data = data["message"]
        if "text" in data:
            message = {
                "chat_id" : data["chat"]["id"],
                "text" : data["text"],
                "message_id" : data["message_id"],
                "user_info" : data["chat"],
            }
            
        elif "audio" in data:
            message = {
                "chat_id" : data["chat"]["id"],
                "audio_id" : data["audio"]["file_id"],
                "audio_name" : data["audio"]["file_name"],
                "message_id" : data["message_id"],
            }      

        elif "video" in data:
            message = {
                "chat_id" : data["chat"]["id"],
                "audio_id" : data["video"]["file_id"],
                "audio_name" : data["video"]["file_name"],
                "message_id" : data["message_id"],
            }     
        else:
            report = True

    elif "callback_query" in data:
        data = data["callback_query"]
        if "data" in data:
            message = {
                "chat_id" : data["message"]["chat"]["id"],
                "message_id" : data["message"]["message_id"],
                "callback" : data["data"],
            }
            
    else:
        report = True

##############
    if report:
        report = Logs(
            def_name = "format_message",
            text = data
        )
        report.save()
        print("LOGS!")
    return message

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
        callback_json = json.loads(callback_query)  
    except:
        pass
    return callback_json

def message_delete(chat_id, message_id):
    data = {
        "chat_id": chat_id,
        "message_id" : message_id
    }
    response = requests.post(f"https://api.telegram.org/bot{TOKEN}/deleteMessage", data)
    return response



