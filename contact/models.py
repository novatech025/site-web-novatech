from django.db import models

class Message_User(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(default = 'kfb@gmail.com')
    message = models.TextField(default = 'message')
    date_send = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

