from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register'),
    path('login/', views.student_login, name='login'),
    path('logout/', views.student_logout, name='logout'),
    path('success/', views.success, name='success'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('', views.home, name='home'),
]