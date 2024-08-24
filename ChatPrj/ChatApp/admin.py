from django.contrib import admin
from .models import * #use * to import everything
# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
