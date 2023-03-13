from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import News, Comment, User, Like, UserRoles


# Register your models here.
#
admin.site.register(News)
admin.site.register(User,UserAdmin)
admin.site.register(Comment)
admin.site.register(Like)
