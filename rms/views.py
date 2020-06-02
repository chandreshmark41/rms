from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import staticfiles

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'About.html')
def hostel(request):
    return render(request,'hostel.html')
def mess(request):
    return render(request,'mess.html')
def lab(request):
    return render(request,'lab.html')
def StudentLogin(request):
    return render(request,'login.html')