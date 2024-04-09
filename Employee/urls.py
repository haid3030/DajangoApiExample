from django.conf.urls import url
from Employee import views

urlpatterns = [
   url(r'^departement/$', views.departementApi),
   url(r'^departement/([0-9]+)$', views.departementApi),
   
   url(r'^employee/$', views.employeeApi),
   url(r'^employee/([0-9]+)$', views.employeeApi),
]

