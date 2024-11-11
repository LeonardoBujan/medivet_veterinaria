from django.urls import path, include
from custom_user.views import UserListView

urlpatterns = [
    path('', UserListView.as_view(), name = 'user'),
    path('create_address/', include('address.urls')),
    path('create_telephone/', include('telephone.urls')),
]