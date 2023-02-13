from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
# Create your views here.

from cliente.models import Person, Cliente

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class PersonListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model= Person
    template_name = "cliente/person/person_list.html"

class PersonCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
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


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
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

class PersonDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Person
    success_url = reverse_lazy('list_person')



class ClienteListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model= Cliente
    template_name = "cliente/cliente/cliente_list.html"

class ClienteCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields = "__all__"

    template_name = "cliente/form.html"
    success_url = "/cliente/list_cliente"

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields = "__all__"

    template_name = "cliente/form.html"
    success_url = "/cliente/list_cliente"

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cliente
    success_url = reverse_lazy('list_cliente')

