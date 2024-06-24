from django.urls import path
from turn.views import TurnListView, TurnCreateView, TurnCreateAttentionView, TurnCreateProfessionalView, TurnCreateDateView, TurnDeleteView

urlpatterns = [
    path('', TurnListView.as_view(), name = 'turn'),
    path('create/', TurnCreateView.as_view(), name = 'create_pet'),
    path('create/<int:id_pet>/attention/', TurnCreateAttentionView.as_view(), name = 'create_attention'),
    path('create/<int:id_pet>/attention/<int:id_attention>/professional/', TurnCreateProfessionalView.as_view(), name = 'create_professional'),
    path('create/<int:id_pet>/attention/<int:id_attention>/professional/<int:id_professional>/date/<str:date>/', TurnCreateDateView.as_view(), name = 'create_date'),

    path('delete/<int:id>/', TurnDeleteView.as_view(), name= 'turn_delete')
]