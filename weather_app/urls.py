from django.urls import path
from .views import WeatherInfoView

urlpatterns = [
    path('weather/', WeatherInfoView.as_view(), name='weather-info'),
]
