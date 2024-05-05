from django.contrib import admin
from employee.models import Employee
 

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age"] 


admin.site.register(Employee, EmployeeAdmin)