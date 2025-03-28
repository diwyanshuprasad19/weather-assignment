curl --location 'http://127.0.0.1:8000/api/v1/weather/?pincode=411014&for_date=2020-12-15'


{
    "status":"success",
    "message":"Data fetched successfully.",
    "data":{
        "pincode":"411014",
        "latitude":18.5685,
        "longitude":73.9158,
        "date":"2020-12-15",
        "temperature":29.05,
        "feels_like":28.57,
        "humidity":39,
        "pressure":1010,
        "description":"scattered clouds"
        }
}
