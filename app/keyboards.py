import json


def main_menu():
    data = {"test":"qq", "res":{"qq":"pp"}}
    keyboard = {
    "inline_keyboard" :  [
        [
            {'text': 'Озвучки', 'callback_data':json.dumps(data)}
        ],
        [
            {'text': 'Каналы и соц сети', 'callback_data': 'info'}
        ],
    ]
}
    return keyboard

def menu_button():
    keyboard= {
        "inline_keyboard" :  [
            [
                {'text': 'Меню', 'callback_data': 'menu'}
            ]
        ]
    }

    return keyboard