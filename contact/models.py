from django.db import models

class utilisateures (models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(default = 'kfb@gmail.com')
    message = models.TextField(default = 'message')

    def __str__(self):
        return self.name

