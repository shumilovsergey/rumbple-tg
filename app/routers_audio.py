from .telegram_def import auth
from .telegram_def import message_send
from .telegram_def import message_delete



def routers_audio(message):

    if auth(message["chat_id"]):
        message_send(
            text= message["audio_id"] + "\n" + message["audio_name"],
            chat_id= message["chat_id"],
            keyboard={}
        )

    else:
        message_delete(message["chat_id"], message["message_id"])

    return