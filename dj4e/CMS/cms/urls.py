from django.contrib import admin

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('CMS/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('past-consult/', views.pastconsult, name='pastconsult'),
    path('lab-reports/', views.report, name='report'),
    path('past-booking/', views.pastbooking, name='pastbooking'),
    path('active-booking/', views.activebooking, name='activebooking'),
    path('doctors/', views.doctors, name='doctors'),
    path('doctors/booking', views.booking, name='booking'),
    path('change/<int:uid>', views.change, name='change'),
    path('forgot/', views.forgot, name='forgot'),
    path('otp/<int:uid>', views.otp, name='otp'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
