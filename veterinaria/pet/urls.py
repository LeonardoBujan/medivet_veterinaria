from django.urls import path
from pet.views import PetListView, PetCreateView, PetEditView, PetDeleteView

urlpatterns = [
    path('', PetListView.as_view(), name = 'pet'),
    path('create/', PetCreateView.as_view(), name = 'pet_create'),
    path('edit/<int:id>/', PetEditView.as_view(), name = 'pet_edit'),
    path('delete/<int:id>/', PetDeleteView.as_view(), name= 'pet_delete')
]