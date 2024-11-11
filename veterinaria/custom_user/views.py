from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from telephone.models import Telephone
from address.models import Address

class UserListView(TemplateView):
    template_name = 'user.html'

    def get(self, request, *args, **kwargs):
        """ Función que permite recuperar los datos del usuario para enviarselo a la vista """
        
        data_user = User.objects.get(id=request.user.id)
        telephone = Telephone.objects.filter(user=request.user.id)
        address = Address.objects.filter(user=request.user.id)
        context = {"name_user": data_user.username, "email": data_user.email, "first_name": data_user.first_name, "last_name": data_user.last_name, "address": address, "telephone": telephone}

        return render(request, self.template_name, context)