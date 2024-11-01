import json
from unittest.mock import patch

from django.urls import reverse
from rest_framework.test import APITestCase

# Create your tests here.


def mock_gemini(text):
    return 'Lorem ipsum'


class ChatTests(APITestCase):
    @patch('gemini.util.Util.gemini_integration', mock_gemini)
    def test_create_chat(self):
        url = reverse('gemini.chat')

        data = {
            'text': ''
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)

        data = {
            'text': 'abc'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response['text_input'], 'abc')
