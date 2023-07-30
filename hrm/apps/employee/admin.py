from django.contrib import admin

from apps.employee.models import Timelog, Employee

# Register your models here.

admin.site.register(Timelog)
admin.site.register(Employee)
