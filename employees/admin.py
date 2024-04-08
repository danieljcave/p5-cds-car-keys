from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'picture',
        'name',
        'job_position',
        'age',
        'bio',
    )

admin.site.register(Employee, EmployeeAdmin)