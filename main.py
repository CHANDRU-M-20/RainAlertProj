import requests
from twilio.rest import Client

OWM_Endpoint="https://api.openweathermap.org/data/2.5/onecall"
api_key="4376142292ba189596a1864858a00d23"
#Twilio account ---
account_sid="ACf13a3d8fe3037cf7a6ee729c12e6927e"
auth_token="824e7d0ffa3de0218fcb342b6d476f95"

# user_count=int(input())
# for user in range(2):
print("Please make sure your Mobile number is already Registered \n")

num=input("Enter your valid Mobile Number ,Must start will country  code eg(+91##########):")


weather_params={
    "lat":11.626260,
    "lon":78.002010,
    "appid":api_key,
    "exclude":"current,minutly,daily"
}
response=requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data=response.json()
#print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice=weather_data["hourly"][:12]

i=0

rain=False
for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
         rain=True




if rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Your Location:The Indian Meteorological Department,the city will see cloudy conditions with very light rain and thundershowers for next few hour,Remember to bring Umberlla ☂️",
        from_='+17204106308',
        to=num
    )

    print(message.sid)
    print("Message send sucessfully..")
else:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Your Location:The Indian Meteorological Department,the city will see good weather conditions,Have a great day",
        from_='+17204106308',
        to=num


    )
    print(message.sid)
    print("Message send sucessfully..")

