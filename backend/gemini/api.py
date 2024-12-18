from rest_framework import generics
from rest_framework.response import Response
import markdown

from .models import Chat
from .serializers import ChatSerializer
from .util import Util


class ChatsAPI(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

    def create(self, request, *args, **kwargs):
        text = request.data["text"]
        output = Util.gemini_integration(text)
        output = markdown.markdown(output)
        serializer = ChatSerializer(data={"text_input": text, "gemini_output": output})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ChatAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
