import json
from .models import Janras
from .models import Artists
from .models import Files

def main_menu():
    data = {
        "sql":"get",
        "g":"1",
        "janra":"?"

    }

    keyboard = {
    "inline_keyboard" :  [
        [
            {'text': 'Озвучки', 'callback_data':json.dumps(data)}
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
                {'text': 'Меню', 'callback_data': json.dumps({"menu":"menu"})}
            ]
        ]
    }

    return keyboard

def sql_keyboard(callback):

    method = "???"  ###????
    group = "???"   ###????
    if group > 1:
        back_button = "???" ###????
    else:
        back_button = "???" ###????

    
    all_elements = "???"    ###????
    element_count = int(len(all_elements))
    first_element_number = (6*(group - 1)) + 1
    amount = element_count - ( 6*group )
    count = 1
    array = []
 
    if amount <= 0:#last group
        for element in all_elements:
            if count >= first_element_number:
                model = element
                model_id = model.id
                model_name = model.name
                array_element = [{'text': model_name, 'callback_data': "???" }] ###????
                array.append(array_element)
            count += 1 

        navigation = [
            {'text': "◀", 'callback_data': json.dumps(back_button)}
        ]       
    else:#not last group
        for element in all_elements:
            last_element_counter = (6*group)+1
            if count >= first_element_number:
                if count < last_element_counter:
                    model = element
                    model_id = model.id
                    model_name = model.name
                    array_element = [{'text': model_name, 'callback_data': "???"}] ###????
                    array.append(array_element)
            count += 1
        next_group = group + 1
        navigation = [
            {'text': "◀", 'callback_data': json.dumps(back_button)},
            {'text': "▶", 'callback_data': "???"}   ###????
        ]

    array.append(navigation)
    keyboard = {
        "inline_keyboard" :  array
    }   
    return keyboard