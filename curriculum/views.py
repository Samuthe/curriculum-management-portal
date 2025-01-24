from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

def home(request):
    return render(request, 'base.html')

def register_student(request):
    return render(request, 'accounts/register.html')

def student_login(request):
    return render(request, 'accounts/login.html')

def student_dashboard(request):
    return render(request, 'accounts/dashboard.html')

def success(request):
    return render(request, 'accounts/success.html')

def student_logout(request):
    return render(request, 'accounts/logout.html')


