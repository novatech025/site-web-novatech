from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('missions/',views.missions,name='missions'),
    path('services/',views.services,name='services')
    # path('contacts/',views.contact,name='contact'),
]