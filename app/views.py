from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .telegram_def import update_parser
from .telegram_def import format_message
from .routers_text import routers_text
from .routers_callback import routers_callback
from .routers_audio import routers_audio

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        update = update_parser(request)
        format = format_message(update)

        if format == "callback":
            callback_query = update.callback_query
        else:
            message = update.message
###################################################

        if format == "text":
            routers_text(message)

        elif format == "audio":   #MODERATOR
            routers_audio(message)
                  
        elif format == "callback":
            routers_callback(callback_query)

    return JsonResponse({'status': 'ok'})






