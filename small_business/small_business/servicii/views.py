from django.shortcuts import render, resolve_url
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from servicii.forms import ServiciiForm
from servicii.models import ServiciiModel


class ServiciiDetailView(DetailView):
    template_name = 'servicii/detalii.html'
    model = ServiciiModel  #Select * from ServiciiModel where pk is id

class ServiciiListView(ListView):
    template_name = 'servicii/all.html'
    model = ServiciiModel

class ServiciiUpdateView(UpdateView):
    form_class = ServiciiForm
    template_name = 'create_update_form.html'
    model = ServiciiModel
    success_url = reverse_lazy('serviciu-all')

class ServiciiDeleteView(DeleteView):
    template_name = 'delete_form.html'
    model = ServiciiModel
    succes_message = "Serviciu Sters cu Succes"
    success_url = reverse_lazy('serviciu-all')

class ServiciiCreateView(CreateView):
    form_class = ServiciiForm
    template_name = 'create_update_form.html'
    model = ServiciiModel
    success_url = reverse_lazy('serviciu-all')