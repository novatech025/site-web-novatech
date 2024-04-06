
from django.urls import path

from .views import index, detail

app_name = "event"
urlpatterns = [
    path("", index, name="index"),
    path("<int:event_id>/", detail, name="detail"),
]


