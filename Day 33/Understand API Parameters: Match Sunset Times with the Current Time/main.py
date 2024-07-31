import requests

from datetime import datetime

MY_LAT = 22.572645
MY_LONG = 88.363892

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}



response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunrise.split("T")[1].split(":")[0])

time_now = datetime.now()

print(time_now)











