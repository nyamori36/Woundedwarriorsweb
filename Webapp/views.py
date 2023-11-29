from django.shortcuts import render

# Create your views here.
#home page
def home(request):
    return render(request,"home.html")

#application
def application(request):
    return render(request,"application.html")

#login
def login(request):
    return render(request,"login.html")




