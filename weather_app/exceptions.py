from rest_framework.exceptions import APIException


class WeatherAPIException(APIException):
    status_code = 500
    default_detail = "An error occurred while processing the request."
    default_code = "error"


class NotFoundException(WeatherAPIException):
    status_code = 404
    default_detail = "Resource not found."
    default_code = "not_found"


class BadRequestException(WeatherAPIException):
    status_code = 400
    default_detail = "Invalid request."
    default_code = "bad_request"
