from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from pet.models import Pet
from type_attention.models import TypeAttention
from professional.models import Professional
from turn.models import Turn

class TurnListView(TemplateView):
    template_name = 'turn.html'

    def get(self, request, *args, **kwargs):
        turn = Turn.objects.filter(user=request.user.id)
        context = { 'turns': turn }
        return render(request, self.template_name, context)


class TurnCreateView(TemplateView):
    template_name = 'create_turn.html'

    def get(self, request):
        pet = Pet.objects.filter(user=request.user.id)
        context = { "pets": pet }
        return render(request, self.template_name, context)

class TurnCreateAttentionView(TemplateView):
    template_name = 'create_attention.html'

    def get(self, request, id_pet):
        type_attention = TypeAttention.objects.all()
        context = { "pets": id_pet, "type_attention": type_attention }
        return render(request, self.template_name, context)

class TurnCreateProfessionalView(TemplateView):
    template_name = 'create_professional.html'

    def get(self, request, id_pet, id_attention):
        professional = Professional.objects.filter(type_attention_id=id_attention)
        context = { "pets": id_pet, "attention": id_attention, "professional": professional }
        return render(request, self.template_name, context)


class TurnCreateDateView(TemplateView):
    template_name = 'create_date.html'

    def get(self, request, id_pet, id_attention, id_professional, date):        
        
        # genera los 6 horarios de atención en los cuales atiende la veterinaria
        init_hour = 9
        list_hours = []

        for x in range(0, 6):
            if str(init_hour).__len__() == 1:
                new_hour_string = "0" + str(init_hour) + ":00"
                list_hours.append(new_hour_string)
                init_hour += 1
            else:
                new_hour_string = str(init_hour) + ":00"
                list_hours.append(new_hour_string)
                init_hour += 1
   
        try:
            turns = Turn.objects.filter(professional=id_professional, date=date)            
            for turn in turns:
                list_hours.remove(str(turn.time)[:5])                
            print(list_hours)
        except:
            print("No se encontro turno asignado para el medico")
        

        context = { "pets": id_pet, "attention": id_attention, "professional": id_professional, "date": date, "hours": list_hours }
        return render(request, self.template_name, context)

    def post(self, request, id_pet, id_attention, id_professional, date):
        pet = get_object_or_404(Pet, pk=id_pet)
        professional = get_object_or_404(Professional, pk=id_professional)
        time = request.POST['hour_check']

        print(time)
        turn = Turn(user=request.user, pet=pet, professional=professional, date=date, time=time)

        try:
            turn.save()
            return redirect('turn')
        except:
            return render(request, 'create_date.html', {
                'msg': "No se pudo crear el turno"})

class TurnDeleteView(TemplateView):
    template_name = 'delete_turn.html'

    def get(self, request, id, *args, **kwargs):
        turn = get_object_or_404(Turn, pk=id)
        context = {'turn_delete': turn}
        return render(request, self.template_name, context)

    def post(self, request, id, *args, **kwargs):        
        turn = get_object_or_404(Turn, pk=id)
        try:
            turn.delete()
            return redirect('turn')
        except:
            return render(request, 'turn.html', {
                'msg': "No se pudo eliminar el turno"})