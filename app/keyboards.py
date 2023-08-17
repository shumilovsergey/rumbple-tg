import json
from .models import Janras
from .models import Artists
from .models import Files

def main_menu():
    audio_data = {
        "sql":"get",
        "g":"1",
        "a_janra":"?",
        "f":"-"
    }

    video_data = {
        "sql":"get",
        "g":"1",
        "v_janra":"?",
        "f":"-"
    }

    keyboard = {
    "inline_keyboard" :  [
        [
            {'text': 'Аудио', 'callback_data':json.dumps(audio_data)}
        ],
        [
            {'text': 'Видео', 'callback_data':json.dumps(video_data)}
        ],
        [
            {'text': 'Каналы и соц сети', 'callback_data': json.dumps({"info":"info"})}
        ],
    ]
}
    return keyboard

def menu_button():
    keyboard= {
        "inline_keyboard" :  [
            [
                {'text': '◀', 'callback_data': json.dumps({"menu":"menu"})}
            ]
        ]
    }
    return keyboard

def sql_keyboard(method, group, all_elements, next_key, navigation):
    first_element_number = (6*(group - 1)) + 1
    last_element_counter = (6*group)+1
    count = 1
    array = []

    for element in all_elements:
        if count >= first_element_number:
            if count < last_element_counter:
                model = element
                model_id = model.id
                model_name = model.name

                data = {
                    "sql":method,
                    "f":model_id,
                    "g":"1",
                    next_key:"?"
                }

                array_element = [{'text': model_name, 'callback_data':json.dumps(data)}] 
                array.append(array_element)
        count += 1

    array.append(navigation)
    keyboard = {
        "inline_keyboard" :  array
    }   
    return keyboard
