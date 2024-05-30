from django.shortcuts import render, HttpResponse
from django.core.mail import mail_admins
from .models import Message_User
from django.contrib import messages


def index(request):
    if request.POST:
        name = request.POST.get('nom')
        email = request.POST.get('mail')
        message = request.POST.get('message')
        new_message_user = Message_User.objects.create(name = name, email = email, message = message)
        new_message_user.save()
        
        print(name)
        print(email)
        print(message)
        
        sujet = "message aux adminitrateur du site de novatech"
        corps_message = f"""
                Nom: {name}
                Email: {email}
                Message: {message}
            """

            # Envoyer le message email aux administrateurs
        mail_admins(
            subject=sujet,
            message=corps_message,
        )
        messages.error(request, "message  envoyer avec succes")
    
    return render(request, 'contact/index.html')

