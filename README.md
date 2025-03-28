# Weather Information API

A Django REST API to fetch and store weather information for a specific pincode and date using the OpenWeather API.  
The API stores location data (pincode, latitude, longitude) and weather data (temperature, humidity, pressure, description, etc.) in a relational database.  

---

## 📌 Features
- Stores location data (pincode, latitude, longitude) and weather data in the database.
- Avoids redundant API calls by caching results.
- Supports test cases for validation and performance testing.
- Follows REST API principles with Class-Based Views (CBVs).
- Organized code structure with separation of concerns (Models, Services, Views, Exceptions, etc.).

---

## 🔥 Requirements
- Python (Version 3.12+)
- Django
- Django REST Framework
- python-dotenv
- requests

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

git clone git@github.com:diwyanshuprasad19/weather-assignment.git
cd weather_info

### Activate Virtual Environment


python -m venv env
source env/bin/activate  # Linux / Mac
.\env\Scripts\activate    # Windows

### Install Dependencies

pip install -r requirements.txt

### Apply Migrations

python manage.py makemigrations
python manage.py migrate

### Run the Server

python manage.py runserver

### Making API Calls (Using Postman or CURL)

Make a GET request to:

http://127.0.0.1:8000/api/v1/weather/?pincode=411014&for_date=2020-10-15

## API Response Format (Example)

Successful Response (Weather Data Found)

{
    "status": "success",
    "message": "Data fetched successfully.",
    "data": {
        "pincode": "411014",
        "latitude": 18.5204,
        "longitude": 73.8567,
        "date": "2020-10-15",
        "temperature": 28.5,
        "feels_like": 30.0,
        "humidity": 78,
        "pressure": 1012,
        "description": "clear sky"
    }
}

# Error Response (Data Not Found / Invalid Pincode)

{
    "status": "error",
    "message": "Resource not found."
}
# Error Response (Invalid Request)

{
    "status": "error",
    "message": "Invalid request."
}

## Testing (TDD)
To run tests, execute:

python manage.py test

