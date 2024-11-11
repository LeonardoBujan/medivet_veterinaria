from django.urls import path
from send_email.views import Contact, ConfirmationEmail

urlpatterns = [
    path('', Contact.as_view(), name='contact'),
]