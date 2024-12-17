from django.shortcuts import render, redirect
from . models import CarBrand,Mechanic,Garage,WashingBay, Contact
from . forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def register(request):
    return render(request, 'auth/register.html', {})
def loginUser(request):
    return render(request, 'auth/login.html', {})

def washingbay(request):
    washingbay = WashingBay.objects.all()
    return render(request, 'washingbay.html', {'washingbay':washingbay})

def repairlocation(request):
    garage = Garage.objects.all()
    return render(request, 'repair.html', {'garage':garage})


def mechanic(request):
    mechanic = Mechanic.objects.all()
    return render(request, "mechanic.html", {'mechanic':mechanic})


def home(request):
    brand = CarBrand.objects.all().order_by('brand_name')
    return render(request, "index.html", {"brand":brand})


def contact(request): 
    return render(request, "contact.html", {})


   

def about(request):
    return render(request, "about.html")
