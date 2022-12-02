from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
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
    return render(request,"register.html")
