from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Location, WeatherData


class WeatherInfoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('weather-info')
        self.valid_pincode = '411014'
        self.valid_date = '2020-10-15'

    def test_missing_pincode_or_date(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_pincode(self):
        response = self.client.get(self.url, {'pincode': '123456', 'for_date': self.valid_date})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_fetch_weather_success(self):
        response = self.client.get(self.url, {'pincode': self.valid_pincode, 'for_date': self.valid_date})
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED])

    def test_database_caching(self):
        self.client.get(self.url, {'pincode': self.valid_pincode, 'for_date': self.valid_date})
        location = Location.objects.filter(pincode=self.valid_pincode).first()
        weather_data = WeatherData.objects.filter(location=location, date=self.valid_date).first()
        self.assertIsNotNone(weather_data)

    def test_invalid_date_format(self):
        response = self.client.get(self.url, {'pincode': self.valid_pincode, 'for_date': 'invalid-date'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
