from django.db import models
from django.core.mail import EmailMessage
# Create your models here.

# manage newsletter
class MonModeleEmail(EmailMessage):
    def __init__(self, sujet, corps, destinataires):
        super().__init__(sujet, corps, 'novatech025@gmail.com', destinataires)
        self.content_subtype = 'html'