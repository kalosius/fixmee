from rest_framework import serializers
from .models import Car, Mechanic

class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = ['name', 'email', 'location', 'experience', 'phone', 'bio', 'dis_img']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'model', 'vehicle_make', 'description', 'image', 'price']