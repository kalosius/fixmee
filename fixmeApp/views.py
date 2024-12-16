from django.shortcuts import render
from . models import CarBrand,Mechanic,Garage,WashingBay

# Create your views here.
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
    
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
