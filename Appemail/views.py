from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages



def index(request):
    return render(request, 'index.html')


def contacto(request):
    if request.method == 'POST':
        name= request.POST['name']
        email= request.POST['email']
        subject= request.POST['subject']
        message= request.POST['message']

        template=render_to_string('email.html',{
            'name':name,
            'email':email,
            'message':message
        })

        
        email=EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            [''] #Aqui va el email desde donde se envian

        )

        email.fail_silently=False
        email.send()

        return redirect('index')