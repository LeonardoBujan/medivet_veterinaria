from django.urls import path
from address.views import AddressCreateView

urlpatterns = [
    path('', AddressCreateView.as_view(), name = 'create_address'),
]