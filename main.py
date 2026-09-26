import os
import requests
from dotenv import load_dotenv

# Загрузить переменные из .env
load_dotenv()

# Получить переменные из .env
API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')
CITY = os.getenv('CITY')
UNITS = os.getenv('UNITS')

# Проверить, что все переменные загружены
if not API_KEY:
    print("Error: API_KEY not found in .env")
    exit(1)

print(f"✓ Configuration loaded successfully!")
print(f"App Name: Weather App")
print(f"API_KEY loaded: {bool(API_KEY)}")  # True/False, но не сам ключ!
print(f"City: {CITY}")
print(f"Units: {UNITS}")


def get_weather(city, api_key, units):
    """Получить погоду через API""" 
    params = {
        'q': city,
        'appid': api_key,
        'units': units
    }
    
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Проверить ошибки
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not fetch weather - {e}")
        return None



def display_weather(data):
    """Красиво вывести погоду"""
    
    if not data:
        return
    
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    
    print(f"\n{'='*50}")
    print(f"Weather in {city}, {country}")
    print(f"{'='*50}")
    print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description.capitalize()}")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("Welcome to Weather App!")
    print("="*50)
    
    weather_data = get_weather(CITY, API_KEY, UNITS)
    display_weather(weather_data)