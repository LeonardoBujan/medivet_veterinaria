from typing import Any
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

class Contact(TemplateView):
    """ Clase utilizada para enviar email de solicitud de contacto del usuario a la veterinaria """
    template_name  = 'contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        subject = request.POST['subject']
        message = request.POST['message']
        email_from = settings.EMAIL_HOST_USER
        email_to = [request.POST['email']]

        send_mail(subject, message, email_from, email_to, fail_silently=False)

        context={'msg': 'La solicitud de contacto ha sido enviada correctamente'}
        return render(request, self.template_name, context)
    

class ConfirmationEmail():   
    """ Clase utilizada para enviar la registración del turno con sus datos por email al usuario """

    def __init__(self, subject, from_email, to, text_context) -> None:        
        self.subject = subject # asunto
        self.from_email = from_email # correo electrónico de la veterinaria
        self.to = to # correo electrónico del usuario
        self.text_content = text_context # mensaje del mail

        
    def create_mail(self, html_content):        
        email = EmailMultiAlternatives(self.subject, self.text_content, self.from_email, [self.to])
        email.attach_alternative(html_content, "text/html")
        email.send()