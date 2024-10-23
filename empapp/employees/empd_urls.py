from django.urls import path
from .views import search_form, search_employees

urlpatterns = [
    path('', search_form, name='search_form'),
    path('results/', search_employees, name='search_employees'),
]
