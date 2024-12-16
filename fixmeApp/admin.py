from django.contrib import admin
from . models import Car, CarBrand

# Register your models here.
@admin.register(CarBrand)
class CarBrand(admin.ModelAdmin):
    ordering = ['brand_name'] 

admin.site.register(Car)
