from .telegram_def import auth
from .telegram_def import message_send
from .telegram_def import message_delete



def routers_video(message):

    if auth(message["chat_id"]):
        message_send(
            text= message["file_id"] + "\n" + message["file_name"],
            chat_id= message["chat_id"],
            keyboard={}
        )

    else:
        message_delete(message["chat_id"], message["message_id"])

    return