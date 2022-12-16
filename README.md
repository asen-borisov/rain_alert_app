This app will send you SMS when it`s about to rain in your local city .

To Customize : 

api_key = "you key"  ( your key from openweather)
MY_LAT = 41.01 ( your personal LAT location)
MY_LON = 21.01 ( Your personal LON location)

SMS : 

account_sid = "your sid"
    auth_token = os.environ["TWILIO_AUTH_TOKEN"] #your token)

    message = client.messages.create(
        body="Rain incoming",
        from_="",  ( from twilio number)
        to=""      (to your number)
