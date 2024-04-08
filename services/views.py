from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Service
from .forms import ServiceForm
from django.contrib.admin.views.decorators import staff_member_required

# View to list all services
def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

# View to add a new service
@staff_member_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added successfully!')
            return redirect('service_list')  # Redirect to the service list page after adding a service
        else:
            messages.error(request, 'Failed to add service. Please ensure the form is valid.')
    else:
        form = ServiceForm()

    template = 'services/add_service.html'
    context = {'form': form}
    return render(request, template, context)

# View to edit an existing service
@staff_member_required
def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated successfully!')
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)

    template = 'services/edit_service.html'
    context = {'form': form, 'service': service}
    return render(request, template, context)

# View to delete an existing service
@staff_member_required
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    messages.success(request, 'Service deleted successfully!')
    return redirect(reverse('service_list'))
