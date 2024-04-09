from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Employee.models import Departements,Employees
from Employee.serializers import DepartementSerializer,EmployeeSerializer
# Create your views here.
@csrf_exempt
def departementApi(request,id=0):
    if request.method == 'GET':
        deppartement = Departements.objects.all()
        deppartements_serializer = DepartementSerializer(deppartement,many=True)
        return JsonResponse(deppartements_serializer.data,safe=False)
    elif request.method == 'POST':
        deppartement_data = JSONParser().parse(request)
        deppartements_serializer = DepartementSerializer(data=deppartement_data)
        if deppartements_serializer.is_valid():
            deppartements_serializer.save()
            return JsonResponse('Added Successfully',safe=False)
        return JsonResponse('Failed to Add',safe=False)
    elif request.method == 'PUT':
         deppartement_data = JSONParser().parse(request)
         deppartement = Departements.objects.get(DepartementId = deppartement_data['DepartementId'])
         deppartements_serializer = DepartementSerializer(deppartement,data=deppartement_data)
         deppartements_serializer == DepartementSerializer(deppartement,data=deppartement_data)
         if deppartements_serializer.is_valid():
             deppartements_serializer.save()
             return JsonResponse('Added Successfully',safe=False)
         return JsonResponse('Failed to Update',safe=False)
    elif request.method == 'DELETE':
         deppartement = Departements.objects.get(DepartementId = id)
         deppartement.delete()
         return JsonResponse('Delete Successfully',safe=False)
     
     
@csrf_exempt
def employeeApi(request,id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse('Added Successfully',safe=False)
        return JsonResponse('Failed to Add',safe=False)
    elif request.method == 'PUT':
         employees_data = JSONParser().parse(request)
         employees = Employees.objects.get(EmployeeId = employees_data['EmployeeId'])
         employees_serializer = EmployeeSerializer(employees,data=employees_data)
         employees_serializer == EmployeeSerializer(employees,data=employees_data)
         if employees_serializer.is_valid():
             employees_serializer.save()
             return JsonResponse('Added Successfully',safe=False)
         return JsonResponse('Failed to Update',safe=False)
    elif request.method == 'DELETE':
         employee = Employees.objects.get(EmployeeId = id)
         employee.delete()
         return JsonResponse('Delete Successfully',safe=False)