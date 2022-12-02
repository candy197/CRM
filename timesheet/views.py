from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,"Timesheet.html")
        else:
            messages.error(request,"Bad Creds!! ")
            return render(request,"index.html")
    return render(request,'index.html')
def rootlogin(request):
    return render(request,"rootlogin.html")
def LeaveApply(request):
    return render(request,"LeaveApply.html")
def Timesheet(request):
    return render(request,"Timesheet.html")
def LeaveReport(request):
    return render(request,"LeaveReport.html")
def TimesheetReport(request):
    return render(request,"TimesheetReport.html")
def OverallReport(request):
    return render(request,"OverallReport.html")
def register(request):
    if request.method == "POST":
        fullname = request.POST['fname'] 
        username =  request.POST['user']
        email = request.POST['email']
        passwd = request.POST['pass']
        myuser = User.objects.create_user(username,email,passwd)
        myuser.fullname_name = fullname
        myuser.save()
        messages.success(request,"Your account has been created")
        return render(request,'index.html')
    else:
        return render(request,"register.html")
