from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError

class Register(TemplateView):
    template_name  = 'register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        if request.POST['password'] == request.POST['repeat_password']:
            try:
                user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.save()
                return redirect('login')
            except IntegrityError:
                return render(request, 'register.html', {
                'msg': 'El usuario ya existe'
            })
        else:
            return render(request, 'register.html', {
                'msg': 'Las contraseñas no coinciden'
            })

    


