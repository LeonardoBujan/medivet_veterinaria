from django.urls import path
from log_off.views import LogoutView

urlpatterns = [
    path('', LogoutView.as_view(), name='logout'),
]