from django.contrib import admin
from django.urls import path,include
from timesheet import views

urlpatterns = [
    
    path("",views.index,name='timesheet')
]