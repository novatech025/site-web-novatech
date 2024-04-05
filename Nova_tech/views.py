from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"Nova_tech/index.html")

def contact(request):
    return render(request,"Nova_tech/contact.html")


# si l'user essaye d'acceder a une branche du site qui n'existe pas
def erreur_404(request,exception):
    return render(request,"Nova_tech/404.html",status=404) # gestion des page not found