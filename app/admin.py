from django.contrib import admin
from .models import Chats
from .models import Moderators
from .models import Janras
from .models import Files
from .models import Artists
from .models import Logs


admin.site.register(Chats)
admin.site.register(Moderators)
admin.site.register(Janras)
admin.site.register(Files)
admin.site.register(Artists)
admin.site.register(Logs)

