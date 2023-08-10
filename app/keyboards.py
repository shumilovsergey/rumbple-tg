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
    if callback["data"]["janra"] == "?":
        all_elements = Janras.objects.all()
        key = "artist"
        navigation_back = 


    elif callback["data"]["artist"] == "?":
        filter = callback["data"]["janra"]
        key = "file"
        all_elements = 
        navigation_back = 

    elif callback["data"]["file"] == "?":
        filter = callback["data"]["artist"]
        key = "none"
        all_elements = 
        navigation_back = 

    group = int(callback["data"]["g"])
    element_count = int(len(all_elements))
    first_element_number = (6*(group - 1)) + 1
    amount = element_count - ( 6*group )
    count = 1
    array = []

    if amount <= 0:#last group
        for model in all_elements:
            if count >= first_element_number:
                model_id = model.id
                model_name = model.name

                data = {
                    "sql":"get",
                    "g":"1",
                    "f": model_id,
                    key:"?"
                }

                array_element = [{'text': model_name, 'callback_data': }]
                array.append(array_element)
            count += 1 

        navigation = [
            {'text': "Назад", 'callback_data':json.dumps(navigation_back)}
        ]     

    else:#not last group
        for element in all_elements:
            last_element_counter = (6*group_number)+1
            if count >= first_element_number:
                if count < last_element_counter:
                    janra = element
                    janra_id = janra.id
                    janra_name = janra.name
                    array_element = [{'text': janra_name, 'callback_data': f'menu_add/{janra_id}'}]
                    array.append(array_element)
            count += 1
        next_group = group_number + 1
        navigation = [
            {'text': "Отмена", 'callback_data': f'menu_add_abort/'},
            {'text': "Еще жанры", 'callback_data': f'menu_add_group_up/{next_group}'}
        ]

    array.append(navigation)
    keyboard = {
        "inline_keyboard" :  array
    }   
    return keyboard    


    return