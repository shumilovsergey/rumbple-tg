from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .telegram_def import format_message
from .routers_text import routers_text
from .routers_callback import routers_callback
from .routers_audio import routers_audio
from .routers_video import routers_video
from .models import Logs

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        message = format_message(request)

        if "text" in message:
            routers_text(message)

        elif "callback" in message:
            routers_callback(message)

        elif "audio_id" in message:
            routers_audio(message)

        elif "video_id" in message:
            routers_video(message)

        else:
            report = Logs(
                def_name = "webhook",
                text = message
            )
            report.save()

    return JsonResponse({'status': 'ok'})






