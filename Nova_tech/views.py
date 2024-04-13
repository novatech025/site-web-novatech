from django.shortcuts import render

from .models import Service


# Create your views here.

def index(request):
    return render(request,"Nova_tech/index.html")

def contact(request):
    return render(request,"Nova_tech/contact.html")

def missions(request):
    return render(request,"Nova_tech/missions.html")


def services(request):
    services=Service.objects.all()
    context={
        'services':services,
        'title':'Nos Services',
    }
    return render(request,"Nova_tech/services.html",context)
# si l'user essaye d'acceder a une branche du site qui n'existe pas

def erreur_404(request,exception):
    return render(request,"Nova_tech/404.html",status=404) # gestion des page not found

