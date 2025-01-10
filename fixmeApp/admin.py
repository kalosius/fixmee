from django.contrib import admin
from .models import Car, CarBrand, Mechanic, Garage, WashingBay, Contact, Message, UserProfile

# Register your models here.

@admin.register(WashingBay)
class WashingBayAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'vehicle_make']

@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    ordering = ['brand_name']

@admin.register(Mechanic)
class MechanicAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'phone', 'email']

@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['mechanic', 'user', 'content', 'timestamp']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile_image']