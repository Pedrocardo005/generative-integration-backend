from django.db import models

# Create your models here.


class Chat(models.Model):
    text_input = models.CharField(max_length=500, null=False, blank=False)
    gemini_output = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.text_input
