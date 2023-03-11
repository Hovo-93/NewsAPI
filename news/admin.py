from django.contrib import admin
from .models import News,Comment,User,Like
# Register your models here.
#
admin.site.register(News)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Like)

