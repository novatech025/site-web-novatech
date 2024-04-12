from django.shortcuts import render, HttpResponse
from .forme import commentaireform
from .models import utilisateures


def index(request):
    forme = commentaireform()
    message = ''
    if request.method == 'POST':
        forme = commentaireform(request.POST or None)
        if forme.is_valid():
            name = request.POST.get('name')
            message = request.POST.get('message')
            new = utilisateures.objects.create(**forme.cleaned_data)
            new.save()
                
            forme = commentaireform()
    
    return render(request, 'contact/index.html', {'forme':forme, 'message':message})

