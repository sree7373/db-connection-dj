from django.contrib import admin
from home .models import *

# Register your models here.

class homeadmin(admin.ModelAdmin):
    servicetitle=('homename','homedescription')
admin.site.register(home,homeadmin)

class roomadmin(admin.ModelAdmin):
    roomservicetitle=('roomname','roomdiscription')
admin.site.register(room,roomadmin)
