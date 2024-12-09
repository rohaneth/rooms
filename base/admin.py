from django.contrib import admin

# Register your models here.
from .models import Room, Mesage,Topic,tryform

admin.site.register(Room)
admin.site.register(Mesage)
admin.site.register(Topic)
admin.site.register(tryform)