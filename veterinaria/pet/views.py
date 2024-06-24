from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from pet.models import Pet
from type_pet.models import TypePet

# Vista de listado de mascotas
class PetListView(TemplateView):    
    template_name = 'pet.html'

    def get(self, request, *args, **kwargs):
        pet = Pet.objects.filter(user=request.user.id)
        context = { 'pets': pet }
        return render(request, self.template_name, context)

        
# Vista de registro de mascotas
class PetCreateView(TemplateView):
    template_name = 'create_pet.html'
    query_pet = ""
    query_type_pet = ""

    def get(self, request, *args, **kwargs):
        type_pet = TypePet.objects.all()
        self.query_type_pet = type_pet
        context = {'type_pet': self.query_type_pet}
        return render(request, self.template_name, context)  


    def post(self, request, *args, **kwargs):
        type_pet = TypePet.objects.get(id=request.POST['type_pet'])
        pet = Pet(user=request.user, type_pet=type_pet, pet_name=request.POST['pet_name'], date_birth_pet=request.POST['date_birth'])
        try:
            pet.save()
            return redirect('pet')
        except:
            return render(request, 'pet.html', {
                'msg': "No se pudo crear la mascota"})
        

# Vista de modificación de mascotas
class PetEditView(TemplateView):
    template_name = 'edit_pet.html'

    def get(self, request, id, *args, **kwargs):
        pet = get_object_or_404(Pet, pk=id)
        type_pet = TypePet.objects.all()
        date_birth = pet.date_birth_pet.strftime("%Y-%m-%d")
        context = {'pet_edit': pet, 'type_pet': type_pet, 'date_birth': date_birth}
        return render(request, self.template_name, context)
    
    def post(self, request, id, *args, **kwargs):        
        pet = get_object_or_404(Pet, pk=id)
        try:
            pet.type_pet=TypePet.objects.get(pk=request.POST['type_pet'])
        except ValueError:
            pet.type_pet=TypePet.objects.get(type_pet_name=request.POST['type_pet'])
            pet.pet_name=request.POST['pet_name']
            pet.date_birth_pet=request.POST['date_birth']
        try:
            pet.save()
            return redirect('pet')
        except:
            return render(request, 'pet.html', {
                'msg': "No se pudo crear la mascota"})

# Vista de eliminación de mascotas
class PetDeleteView(TemplateView):
    template_name = 'delete_pet.html'

    def get(self, request, id, *args, **kwargs):
        pet = get_object_or_404(Pet, pk=id)
        type_pet = TypePet.objects.all()
        date_birth = pet.date_birth_pet.strftime("%Y-%m-%d")
        context = {'pet_delete': pet, 'type_pet': type_pet, 'date_birth': date_birth}
        return render(request, self.template_name, context)

    def post(self, request, id, *args, **kwargs):        
        pet = get_object_or_404(Pet, pk=id)
        try:
            pet.delete()
            return redirect('pet')
        except:
            return render(request, 'pet.html', {
                'msg': "No se pudo eliminar la mascota"})