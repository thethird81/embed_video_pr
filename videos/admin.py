from django.contrib import admin


from .models import Video
from .models import Member

admin.site.register(Video)
admin.site.register(Member)
