from django.contrib import admin
from mysite.models import EmployeeModel

class EmployeeAdmin(admin.ModelAdmin):
    pass
admin.site.register(EmployeeModel, EmployeeAdmin)