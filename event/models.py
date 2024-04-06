from django.db import models
from django.contrib.auth.models import User
# from core.models import CategoryModel
from tinymce.models import HTMLField
 

class EventModel(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255, unique=True, verbose_name="titre")
    subtitle = models.CharField(blank=False, null=False, default="", max_length=255, verbose_name="texte présentatif")
    description = HTMLField(max_length=50000, verbose_name="description de l'évènement")
    start_at = models.DateTimeField(blank=False, null=True, verbose_name="date de début")
    end_at = models.DateTimeField(blank=False, null=True, verbose_name="date de fin")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="Date d'ajout")
    published = models.BooleanField(default=True, verbose_name="publié")
    illustration_image = models.ImageField(blank=False, null=False, upload_to='images/events/%Y/%m/%d', verbose_name="image d'illustration")
    illustration_video = models.CharField(max_length=1000, blank=True, null=True, verbose_name="lien de la vidéo d'illustration")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "évènement"
        verbose_name_plural = "évènements"


