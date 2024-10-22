from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from students.models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['name', 'age', 'email']
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['name', 'age', 'email']
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
