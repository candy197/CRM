from django.contrib import admin
from django.urls import path,include
from timesheet import views

urlpatterns = [

     path("",views.index,name='timesheet'),
     path("rootlogin",views.rootlogin,name='timesheet'),
     path("index",views.index,name='timesheet'),
     path("LeaveApply",views.LeaveApply,name='timesheet'),
     path("Timesheet",views.Timesheet,name='timesheet'),
     path("LeaveReport",views.LeaveReport,name='timesheet'),
     path("TimesheetReport",views.TimesheetReport,name='timesheet'),
     path("OverallReport",views.OverallReport,name='timesheet'),
     path("register",views.register,name='timesheet'),
    
   
]