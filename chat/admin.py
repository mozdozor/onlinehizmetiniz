from django.contrib import admin

from chat.models import Room, peerInformations

# Register your models here.




admin.site.register(peerInformations)
admin.site.register(Room)