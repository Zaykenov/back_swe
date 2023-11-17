from django.db import models
from accounts.models import CustomUser
from django_chat.models import Room


# Create your models here.
class Dispatcher(CustomUser):
    def __str__(self) -> str:
        return self.email

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.name} to {self.receiver.name} - {self.content}'