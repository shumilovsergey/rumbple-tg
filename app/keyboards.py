import json


def main_menu():
    data = {
        "sql":"get",
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