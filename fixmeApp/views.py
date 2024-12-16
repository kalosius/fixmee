from django.shortcuts import render
from . models import CarBrand

# Create your views here.
def home(request):
    brand = CarBrand.objects.all().order_by('brand_name')
    return render(request, "index.html", {"brand":brand})

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
