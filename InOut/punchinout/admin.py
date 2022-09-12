from django.contrib import admin

# Register your models here.
from punchinout.models import timein,timeout,User

admin.site.register([timein,timeout,User])