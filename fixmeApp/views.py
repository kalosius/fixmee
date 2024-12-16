from django.shortcuts import render
from . models import CarBrand,Mechanic

# Create your views here.
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
