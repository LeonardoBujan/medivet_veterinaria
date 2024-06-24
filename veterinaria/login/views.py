from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):                    
        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        # Valida si el usuario esta registrado en la BD
        if user is not None:
            # Inicia la sesion del usuario
            login(request, user)
            return redirect('home')
        else:
            return render(request, self.template_name, {
                'msg': 'Usuario y/o contraseña incorrectos'
            })
    