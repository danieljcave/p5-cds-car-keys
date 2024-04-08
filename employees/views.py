from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added employee!')
            return redirect('index')  # Redirect to the index page after adding an employee
        else:
            messages.error(request, 'Failed to add employee. Please ensure the form is valid.')
    else:
        form = EmployeeForm()

    template = 'employee/add_employee.html'
    context = {'form': form}
    return render(request, template, context)
