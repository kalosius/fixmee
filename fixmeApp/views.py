from django.shortcuts import render, redirect
from . models import CarBrand,Mechanic,Garage,WashingBay, Car, Contact
from . forms import ContactForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .serializers import MechanicSerializer, CarSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Dashboard
def dashboard(request):
    garages = Garage.objects.all()
    mechanics = Mechanic.objects.all()
    cars = Car.objects.all()
    bays = WashingBay.objects.all()
    contacts = Contact.objects.all()
    return render(request, 'auth/dashboard.html', {
        'garages': garages, 
        'mechanics': mechanics, 
        'cars': cars, 
        'bays': bays,
        'contacts': contacts,
        'garage_count': garages.count(),
        'mechanic_count': mechanics.count(),
        'car_count': cars.count(),
        'contact_count': contacts.count(),
        'garage_created_at': garages.first().created_at if garages.exists() else None,
        'mechanic_created_at': mechanics.first().created_at if mechanics.exists() else None,
        'car_created_at': cars.first().created_at if cars.exists() else None,
        'bay_created_at': bays.first().created_at if bays.exists() else None
    })


# https://youtu.be/i5JykvxUk_A
# Api for mechanic and cars
@api_view(['GET', 'POST'])
def mechanic_list(request):
    #  get all the mechanics
    # serialize them
    # return json
    if request.method == 'GET':
        mechanic = Mechanic.objects.all()
        serializer = MechanicSerializer(mechanic, many=True)
        # return JsonResponse({'mechanic':serializer.data}, safe=False)
        return JsonResponse({'mechanic':serializer.data})
    
    if request.method == 'POST':
        serializer = MechanicSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def mechanic_detail(request, id):
    try:
        mechanic = Mechanic.objects.get(pk=id)
    except Mechanic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
       serializer = MechanicSerializer(mechanic)
       return JsonResponse({'mechanic':serializer.data})
    
    elif request.method == 'PUT':
        serializer = MechanicSerializer(mechanic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        pass
     
     
def car_api(request):
     car = Car.objects.all()
     serializer = CarSerializer(car, many=True)
    #  return JsonResponse({"car":serializer.data}, safe=False)
     return JsonResponse({"car":serializer.data})


def register(request):
        form = UserRegistrationForm()
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False) 
                user.set_password(form.cleaned_data['password'])
                user.save()
                messages.success(request, 'Account Created Successfully!')
                return redirect('login')
            else:
                messages.error(request, 'An error occured! Pease Try again!')
                form = UserRegistrationForm()
        return render(request, 'auth/register.html', {'form': form})



def loginUser(request):
        if request.method == "POST":
            username = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ("You Have Been Logged In!"))
                return redirect('home')
            else:
                messages.success(request, ("There was an error, please try again..."))
                return redirect('login')
        else:
            return render(request, 'auth/login.html', {})


@login_required       
def logout_user(request):
	logout(request)
	messages.success(request, ("You have been logged out...Thanks for stopping by..."))
	return redirect('home')

@login_required
def washingbay(request):
    washingbay = WashingBay.objects.all()
    return render(request, 'washingbay.html', {
        'washingbay': washingbay,
        'washingbay_count': washingbay.count(),
        'washingbay_created_at': washingbay.first().created_at if washingbay.exists() else None
    })

@login_required
def repairlocation(request):
    garage = Garage.objects.all()
    return render(request, 'repair.html', {
        'garage': garage,
        'garage_count': garage.count(),
        'garage_created_at': garage.first().created_at if garage.exists() else None
    })


def mechanic(request):
    mechanic = Mechanic.objects.all()
    return render(request, "mechanic.html", {
        'mechanic': mechanic,
        'mechanic_count': mechanic.count(),
        'mechanic_created_at': mechanic.first().created_at if mechanic.exists() else None
    })


def about_mechanic(request, id):
    mechanic = Mechanic.objects.get(pk=id)
    return render(request, 'mechanicdetails.html', {'mechanic':mechanic})


def home(request):
    brand = CarBrand.objects.all().order_by('brand_name')
    return render(request, "index.html", {
        "brand": brand,
        'brand_count': brand.count(),
        'brand_created_at': brand.first().created_at if brand.exists() else None
    })


def contact(request):
    if request.method == "POST": 
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message Submitted!")
        else:
            messages.success(request, "There was an error in the form")
            form = ContactForm()
    return render(request, "contact.html")


   

def about(request):
    return render(request, "about.html")
