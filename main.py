import requests

api_key = "you key"
END_APY = "https://api.openweathermap.org/data/2.5/weather"
MY_LAT = 41.01
MY_LON = 21.01

param = {
    "lat" : MY_LAT,
    "lon" : MY_LON,
    "appid" : api_key,
}


api = requests.get(END_APY, params=param)
api.raise_for_status()
data = api.json()
is_rain = int(data["weather"][0]["id"])

will_rain = False

if is_rain < 700:
    will_rain = True

if will_rain:
    import os
    from twilio.rest import Client
    account_sid = "your sid"
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Rain incoming",
        from_="",
        to=""



