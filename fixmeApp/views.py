from django.shortcuts import render, redirect
from . models import CarBrand,Mechanic,Garage,WashingBay
from . forms import ContactForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


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
    return render(request, 'washingbay.html', {'washingbay':washingbay})

@login_required
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
