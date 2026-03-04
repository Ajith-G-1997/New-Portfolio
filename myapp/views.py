from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'base.html')

def AboutPage(request):
    return render(request,'about.html')
def Resume(request):
    return render(request,'resume.html')
def Services(request):
    return render(request,'services.html')
def Portfolio(request):
    return render(request,'portfolio.html')
def contact(request):
    return render(request,'contact.html')