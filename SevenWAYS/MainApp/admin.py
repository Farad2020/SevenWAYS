from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Place)
admin.site.register(WorkTime)
admin.site.register(PlaceImages)
admin.site.register(Review)