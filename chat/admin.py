from django.contrib import admin
from .models import ChatGroup, GroupMessage


admin.site.register(ChatGroup)
class ChatGroupAdmin(admin.ModelAdmin):
    list_display = ['group_name']
    search_fields = ['group_name']

admin.site.register(GroupMessage)
class GroupMessageAdmin(admin.ModelAdmin):
    list_display = ['group', 'author', 'body', 'created']
    list_filter = ['group', 'author', 'created']
    search_fields = ['body']
