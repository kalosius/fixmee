from django.utils import timezone
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.contrib.auth.models import User

# Create your models here.
class WashingBay(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Garage(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Mechanic(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(validators=[EmailValidator(message="Please enter a valid email address")])
    location = models.CharField(max_length=30)
    experience = models.SmallIntegerField(default=0)
    phone = models.CharField(max_length=14, validators=[MinLengthValidator(10), MaxLengthValidator(14)])
    bio = models.CharField(max_length=100, null=True, blank=True)
    dis_img = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    

class CarBrand(models.Model):
    brand_name = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.brand_name


class Car(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    model = models.CharField(max_length=20, null=True, blank=True )
    vehicle_make = models.ForeignKey(CarBrand, on_delete=models.CASCADE,null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=14, validators=[MinLengthValidator(10), MaxLengthValidator(14)])
    email = models.EmailField(validators=[EmailValidator(message="Please enter a valid email address")])
    message = models.CharField(max_length=200)


class Message(models.Model):
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.user.username} to {self.mechanic.name}'