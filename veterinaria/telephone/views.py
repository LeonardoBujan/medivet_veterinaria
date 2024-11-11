from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from telephone.models import Telephone

class TelephoneCreateView(TemplateView):
    pass
    # template_name = 'create_telephone.html'

    def get(self, request, *args, **kwargs):
        return render (request, 'create_telephone.html')
    
    def post(self, request, *args, **Kwargs):
        country_code = request.POST['country_code']
        area_code = request.POST['area_code']
        telephone_number = request.POST['telephone_number']

        telephone = Telephone(user=request.user, country_code=country_code, area_code=area_code, telephone_number=telephone_number)

        try:
            telephone.save()
            return redirect('user')
        except:
            print("No se pudo grabar el teléfono")