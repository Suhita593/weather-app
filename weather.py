import requests

API_KEY = "05eec931105e486ee6126801d4b0c236"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city) :
    #params - information I am sending with the request
    params = {"q":city, "appid" : API_KEY, "units" : "metric"}
    response = requests.get(BASE_URL, params = params)
    #the above code sends requests to the OpenWeatherMap and waits for the response

    if response.status_code == 200 :
     data = response.json() #this converts the response to a Python dictionary which is easy to work with
     city_name = data["name"]
     temp = data["main"]["temp"]
     weather = data["weather"][0]["description"]
     humidity = data["main"]["humidity"]

     print(f"\nWeather in {city_name}:")
     print(f"Temperature: {temp}")
     print(f"Condition: {weather.capitalize()}")
     print(f"Humidity: {humidity}%\n")

    else :
     print("Error : City not found!")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)

