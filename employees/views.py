from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm
from django.contrib.admin.views.decorators import staff_member_required

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})

@staff_member_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added employee!')
            return redirect('employee_list')  # Redirect to the index page after adding an employee
        else:
            messages.error(request, 'Failed to add employee. Please ensure the form is valid.')
    else:
        form = EmployeeForm()

    template = 'employee/add_employee.html'
    context = {'form': form}
    return render(request, template, context)


@staff_member_required
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee Updated!')
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    template = 'employee/edit_employee.html'
    context = {
        'form': form,
        'employee': employee,
    }

    return render(request, template, context)


@staff_member_required
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    messages.success(request, 'Employee deleted!')
    return redirect(reverse('employee_list'))
