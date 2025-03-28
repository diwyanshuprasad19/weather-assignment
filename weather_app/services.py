import requests
from .models import Location, WeatherData
from .exceptions import WeatherAPIException, NotFoundException
from .constants import RESPONSE_MESSAGES
from django.conf import settings


class WeatherService:

    @staticmethod
    def get_or_create_location(pincode):
        try:
            location = Location.objects.get(pincode=pincode)
        except Location.DoesNotExist:
            geocoding_url = f"https://api.openweathermap.org/geo/1.0/zip?zip={pincode},IN&appid={settings.OPENWEATHER_API_KEY}"
            response = requests.get(geocoding_url)
            if response.status_code != 200:
                raise WeatherAPIException(detail=RESPONSE_MESSAGES['INVALID_REQUEST'])

            data = response.json()
            if 'lat' not in data or 'lon' not in data:
                raise NotFoundException(detail=RESPONSE_MESSAGES['DATA_NOT_FOUND'])

            location = Location.objects.create(
                pincode=pincode,
                latitude=data['lat'],
                longitude=data['lon']
            )
        return location

    @staticmethod
    def get_weather_data(location, date):
        try:
            weather = WeatherData.objects.get(location=location, date=date)
            return weather
        except WeatherData.DoesNotExist:
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
            response = requests.get(weather_url)

            if response.status_code != 200:
                raise WeatherAPIException(detail=RESPONSE_MESSAGES['SERVER_ERROR'])

            data = response.json()

            weather = WeatherData.objects.create(
                location=location,
                date=date,
                temperature=data['main']['temp'],
                feels_like=data['main']['feels_like'],
                humidity=data['main']['humidity'],
                pressure=data['main']['pressure'],
                description=data['weather'][0]['description']
            )
            return weather
