from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:slug>/', views.services_detail, name='services_detail'),
    path('doctor/<slug:slug>/', views.doctors_detail, name='doctors_detail'),
    path('doctors/', views.doctors, name='doctors'),
    path('book/', views.book, name='book'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sign-up/', views.sign_up, name='sign_up'),
]