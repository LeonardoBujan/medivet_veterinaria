from django.urls import path
from register.views import Register

urlpatterns = [
    path('', Register.as_view(), name='register'),
]