from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from address.models import Address

class AddressCreateView(TemplateView):
    template_name = 'create_address.html'

    def get(self, request, *args, **kwargs):
        return render (request, self.template_name)
    
    def post(self, request, *args, **Kwargs):
        street = request.POST['street']
        number = request.POST['number']
        floor = request.POST['floor']
        deparment = request.POST['deparment']

        address = Address(user=request.user, street=street, number=number, floor=floor, deparment=deparment)

        try:
            address.save()
            return redirect('user')
        except:
            print("No se pudo grabar el domicilio")
