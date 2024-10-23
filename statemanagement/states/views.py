from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import State
from .forms import StateForm

class StateListView(ListView):
    model = State
    template_name = 'states/state_list.html'
    context_object_name = 'states'

class StateDetailView(DetailView):
    model = State
    template_name = 'states/state_detail.html'
    context_object_name = 'state'

class StateCreateView(CreateView):
    model = State
    form_class = StateForm
    template_name = 'states/state_form.html'
    success_url = reverse_lazy('state-list')

class StateUpdateView(UpdateView):
    model = State
    form_class = StateForm
    template_name = 'states/state_form.html'
    success_url = reverse_lazy('state-list')

class StateDeleteView(DeleteView):
    model = State
    template_name = 'states/state_confirm_delete.html'
    success_url = reverse_lazy('state-list')
