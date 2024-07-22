import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        
        weather_report = f"Temperature: {temperature}°C\n"
        weather_report += f"Atmospheric Pressure: {pressure} hPa\n"
        weather_report += f"Humidity: {humidity}%\n"
        weather_report += f"Description: {description}\n"
        
        return weather_report
    else:
        return "City Not Found!"

# Replace 'your_api_key' with your actual API key
api_key = "your_api_key"
city = input("Enter city name: ")
print(get_weather(city, api_key))
