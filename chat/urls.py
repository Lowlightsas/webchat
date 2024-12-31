from django.urls import path
from .views import *
app_name='chat'
urlpatterns = [
    path('chat/', chat_view, name='home'),
    path('base/', base, name='base'),
]
