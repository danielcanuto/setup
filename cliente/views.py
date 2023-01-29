from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
# Create your views here.

from cliente.models import Person, Cliente


class PersonListView(ListView):
    model= Person
    template_name = "cliente/person/person_list.html"

class PersonCreateView(CreateView):
    model = Person
    fields = [
        'name',
        'birthday',
        'bio',
        'photo',
        'cpf',
        'rg',
        'sexo'
    ]
    template_name = "cliente/form.html"
    success_url = "/cliente/list_person"


class PersonUpdateView(UpdateView):
    model = Person
    fields = [
        'name',
        'birthday',
        'bio',
        'photo',
        'cpf',
        'rg',
        'sexo'
    ]
    template_name = "cliente/form.html"
    success_url = "/cliente/list_person"

class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('list_person')



class ClienteListView(ListView):
    model= Cliente
    template_name = "cliente/cliente/cliente_list.html"

class ClienteCreateView(CreateView):
    model = Cliente
    fields = [
        'person',
        'telefone',
        'email',
        'cidade_estado',
        'endereco',
        'numero',
        'bairro',
        'cep'
    ]

    template_name = "cliente/form.html"
    success_url = "/cliente/list_cliente"

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = [
        'person',
        'telefone',
        'email',
        'cidade_estado',
        'endereco',
        'numero',
        'bairro',
        'cep'
    ]

    template_name = "cliente/form.html"
    success_url = "/cliente/list_cliente"

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('list_cliente')

