from django.urls import path
from telephone.views import TelephoneCreateView

urlpatterns = [
    path('', TelephoneCreateView.as_view(), name = 'create_telephone'),
]