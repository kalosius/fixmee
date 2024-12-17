from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('mechanic/', views.mechanic, name="mechanic"),
    path('repairlocation/', views.repairlocation, name="repairlocation"),
    path('washingbay/', views.washingbay, name="washingbay"),
    path('login/', views.loginUser, name="login"),
    path('register/', views.register, name="register"),
]