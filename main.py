import requests
import os
from twilio.rest import Client

api_key = YOUR_API_KEY
api_call = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = YOUR_API_SID
auth_token = YOUR_AUTH_TOKEN

weather_params = {
    "lat": -22.016720,
    "lon": -47.891972,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(api_call, params = weather_params)

response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

rain_flag = False

for hour in weather_slice:
    if hour["weather"][0]["id"] < 700:
        rain_flag = True
        
if rain_flag:        
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an ☂️",
                     from_=TEL_FROM_TWILIO, #aqui entra o telefone do twilio
                     to= YOUR_TEL_NUMBER #aqui é o teleofne pra onde vai a mensagem
                 )
    print(message.status)






