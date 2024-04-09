from rest_framework import serializers
from Employee.models import Departements,Employees

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departements
        fields=('DepartmentId','DepartementName')
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields=('EmployeeId','EmployeeName','Departement','DateOfJoining','PhotoFileName')     