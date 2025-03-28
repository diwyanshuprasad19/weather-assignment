from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import WeatherService
from .exceptions import WeatherAPIException, NotFoundException, BadRequestException
from .constants import RESPONSE_MESSAGES, SUCCESS

class WeatherInfoView(APIView):
    def get(self, request):
        pincode = request.GET.get('pincode')
        date = request.GET.get('for_date')

        if not pincode or not date:
            raise BadRequestException(detail=RESPONSE_MESSAGES['INVALID_REQUEST'])

        try:
            location = WeatherService.get_or_create_location(pincode)
            weather_data = WeatherService.get_weather_data(location, date)

            data = {
                "status": SUCCESS,
                "message": RESPONSE_MESSAGES['DATA_FOUND'],
                "data": {
                    "pincode": location.pincode,
                    "latitude": location.latitude,
                    "longitude": location.longitude,
                    "date": date,
                    "temperature": weather_data.temperature,
                    "feels_like": weather_data.feels_like,
                    "humidity": weather_data.humidity,
                    "pressure": weather_data.pressure,
                    "description": weather_data.description
                }
            }
            return Response(data, status=status.HTTP_200_OK)
        except (WeatherAPIException, NotFoundException, BadRequestException) as e:
            return Response({"status": "error", "message": str(e)}, status=e.status_code)
