
from rest_framework import  viewsets
from django.shortcuts import render

from employee.models import Employee
from employee.serializer import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer