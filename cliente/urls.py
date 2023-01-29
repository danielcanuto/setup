from django.urls import path
from cliente.views import ClienteCreateView, ClienteListView, ClienteUpdateView, ClienteDeleteView
from cliente.views import PersonCreateView, PersonListView, PersonUpdateView, PersonDeleteView

urlpatterns = [

    path('list_cliente/', ClienteListView.as_view(), name="list_cliente"),
    path('create_cliente/', ClienteCreateView.as_view(), name="create_cliente"),
    path('update_cliente/<int:pk>', ClienteUpdateView.as_view(), name="update_cliente"),
    path('delete_cliente/<int:pk>', ClienteDeleteView.as_view(), name="delete_cliente"),
    

    path('list_person/', PersonListView.as_view(), name="list_person"),
    path('create_person/', PersonCreateView.as_view(), name="create_person"),
    path('update_person/<int:pk>', PersonUpdateView.as_view(), name="update_person"),
    path('delete_person/<int:pk>', PersonDeleteView.as_view(), name="delete_person"),
]
