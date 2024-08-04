import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_phone = os.getenv("TWILIO_PHONE_FROM")
to_phone = os.getenv("PHONE_TO")

weather_params = {
    "lat": 22.572645,
    "lon": 88.363892,
    "appid": api_key,
    "cnt": 4,
}

responses = requests.get(OWM_Endpoint, params=weather_params)
responses.raise_for_status()
weather_data = responses.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_=from_phone,
        to=to_phone
    )
    print(message.status)
