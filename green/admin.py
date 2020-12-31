from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import myuser,location


admin.site.register(myuser,UserAdmin)

admin.site.register(location)
