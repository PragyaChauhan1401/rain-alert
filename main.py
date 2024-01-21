import requests
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
apikey = "70d8a0e00a97db914d9e32235bfeac90"
account_sid = "twillo_acc_sid"
auth_token = "your authcode"
weather_params = {
    "lat": 31.224020,
    "lon": 75.770798,
    "appid": apikey,
    "cnt": 4
}

response = requests.get(endpoint, params=weather_params)
print(response.status_code)
data = response.json()

will_rain = False
for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

client = Client(account_sid, auth_token)


if will_rain:
    print("Bring an Umbrella")
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella☂️",
        from_='+14154085538',
        to='your verified number'
    )


