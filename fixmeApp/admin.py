from django.contrib import admin
from . models import Car, CarBrand,Mechanic,Garage,WashingBay,Contact

# Register your models here.

 
@admin.register(WashingBay)
class WashingBay(admin.ModelAdmin):
    list_display = ['name', 'location']


@admin.register(Car)
class Car(admin.ModelAdmin):
    list_display = ['name','model','vehicle_make']

@admin.register(CarBrand)
class CarBrand(admin.ModelAdmin):
    ordering = ['brand_name'] 

# Creating Table columns in the admin area
@admin.register(Mechanic)
class Mechanic(admin.ModelAdmin):
    list_display = ['name', 'location', 'phone', 'email']

@admin.register(Garage)
class Garage(admin.ModelAdmin):
    list_display = ['name', 'location']


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ['name']