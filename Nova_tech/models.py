from django.db import models
from django.core.mail import EmailMessage
# Create your models here.

# manage newsletter
class MonModeleEmail(EmailMessage):
    def __init__(self, sujet, corps, destinataires):
        super().__init__(sujet, corps, 'novatech025@gmail.com', destinataires)
        self.content_subtype = 'html'

class Service(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False,verbose_name='Titre')
    content=models.TextField(verbose_name='Description')
    image=models.ImageField(upload_to='images/services',blank=True,null=True)

    def __str__(self):
        return self.title

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url