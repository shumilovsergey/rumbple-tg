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
    data = json.loads(request.body.decode('utf-8'))
    report = False

    if "message" in data:
        data = data["message"]

        if "text" in data:
            # type = "message"
            # chat_id = 
            # text = 
            # user_name = 
            # message_id = 
            pass
        else:

            report = True

    elif "callback_query" in data:
        data = data["callback_query"]
        if "data" in data:
            type = "callback"
            chat_id = data["from"]["chat_id"]
            message_id = data["message"]["message_id"]
            data = data["data"]


    else:
        report = True

##############
    if report:
        report = Logs(
            def_name = "format_message",
            text = data
        )
        report.save()

    return data

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





