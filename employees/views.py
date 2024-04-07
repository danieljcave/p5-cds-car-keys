from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})

@staff_member_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})
