from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from gemini.api import ChatAPI, ChatsAPI

urlpatterns = [
    path('chat/', ChatsAPI.as_view(), name='gemini.chat'),
    path('chat/<int:pk>/', ChatAPI.as_view(), name='gemini.chat-detail'),
    path('chat/schema/', SpectacularAPIView.as_view(), name='spectacular.schema'),
    path('chat/schema/swagger-ui/', SpectacularSwaggerView.as_view(
        url_name='spectacular.schema'), name='spectacular.swagger-ui')
]
