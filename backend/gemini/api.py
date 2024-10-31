from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics
from .serializers import ChatSerializer
from gemini.models import Chat


class ChatsAPI(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()


class ChatAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
