from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class TestimonyModel(models.Model):
    content = models.TextField(blank=False, null=False, verbose_name="Contenu", max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Auteur du témoignage")
    is_visible = models.BooleanField(default=False, null=False, blank=False, verbose_name="Est-ce visible sur le site ?")
    last_updated = models.DateTimeField(auto_now_add=True, verbose_name="Modifié le")
    created_at = models.DateField(blank=True, auto_now=True, null=True, verbose_name="Créé le")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Témoignage"
    
    def save(self, *args, **kwargs):
        self.last_updated = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.content[:100] + "..."
    

