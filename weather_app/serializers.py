from rest_framework import serializers
from .models import Location, WeatherData

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['pincode', 'latitude', 'longitude']


class WeatherDataSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = WeatherData
        fields = ['location', 'date', 'temperature', 'feels_like', 'humidity', 'pressure', 'description']
