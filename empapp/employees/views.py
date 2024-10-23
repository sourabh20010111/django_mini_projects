from django.shortcuts import render

# Create your views here.
from .models import Employee

def search_form(request):
    return render(request, 'employees/search_form.html')

def search_employees(request):
    if request.method == 'POST':
        lookup_type = request.POST.get('lookup_type')
        search_string = request.POST.get('search_string', '').strip()
        age_number = request.POST.get('age_number', '').strip()

        results = []
        if lookup_type == 'startswith':
            results = Employee.objects.filter(fname__startswith=search_string)
        elif lookup_type == 'contains':
            results = Employee.objects.filter(fname__icontains=search_string)
        elif lookup_type == 'lte' and age_number.isdigit():
            results = Employee.objects.filter(age__lte=int(age_number))

        return render(request, 'employees/search_results.html', {'results': results})

    return render(request, 'employees/search_form.html')
