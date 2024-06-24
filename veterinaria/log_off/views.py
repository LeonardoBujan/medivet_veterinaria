from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect

class LogoutView(TemplateView):
    template_name = 'home.html'
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')