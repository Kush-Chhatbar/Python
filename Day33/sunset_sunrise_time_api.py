import requests
import datetime as dt
MY_LAT = 23.020343
MY_LONG = 72.578945

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")

time_now = dt.datetime.now()
current_time = time_now.hour
print(f"Current time: {current_time}")
