from django.db import models

# Create your models here.
class Departements(models.Model):
    DepartmentId   = models.AutoField(primary_key=True)
    DepartementName = models.CharField(max_length = 500)
    
class Employees(models.Model):
    EmployeeId  = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length = 500)
    Departement = models.CharField(max_length = 500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length = 500)
    
    