from django.db import models

# Create your models here.
class CarBrand(models.Model):
    brand_name = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.brand_name


class Car(models.Model):
    model_name = models.CharField(max_length=50, null=True, blank=True)
    vehicle_make = models.ForeignKey(CarBrand, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.model_name
