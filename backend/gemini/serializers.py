from rest_framework import serializers
from gemini.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'text_input', 'gemini_output')
