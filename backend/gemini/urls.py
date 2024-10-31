from django.urls import path
from gemini.api import ChatsAPI, ChatAPI

urlpatterns = [
    path('chat/', ChatsAPI.as_view(), name='gemini.chat'),
    path('chat/<int:pk>/', ChatAPI.as_view(), name='gemini.chat-detail')
]
