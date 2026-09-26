# Weather App

A simple Python application that fetches and displays current weather information using the OpenWeatherMap API.

## Features

- Fetch real-time weather data
- Display temperature, humidity, and weather description
- Load configuration from environment variables
- Secure API key storage

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/weather-app.git
   cd weather-app

   ```

2. ```
   Create virtual environment
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies
   pip install -r requirements.txt
4. Setup environment variables
   cp .env.example .env

Edit .env and fill in your values:

API_KEY: Get free key from https://openweathermap.org/api
CITY: City name (e.g., "Moscow")
UNITS: Temperature units ("metric" for Celsius, "imperial" for Fahrenheit)

USAGE python main.py
python: can't open file '/Users/katana/main.py': [Errno 2] No such file or directory

# Expected output:

# Welcome to Weather App!

✓ Configuration loaded successfully!
App Name: Weather App
API_KEY loaded: True
City: Moscow
Units: metric

==================================================
Weather in Moscow, RU
==================================================
Temperature: 15°C (feels like 14°C)
Humidity: 65%
Description: Partly cloudy
==================================================

Environment Variables
Create .env file with:

API_KEY - Your OpenWeatherMap API key (required)
API_URL - Weather API endpoint (optional, default provided)
CITY - City name to fetch weather for (optional, default: Moscow)
UNITS - Temperature units: "metric" (Celsius) or "imperial" (Fahrenheit)
See .env.example for template.

Requirements
requests
python-dotenv
See requirements.txt for exact versions.

License
MIT License

Author
Your Name

Notes
Never commit .env file - it contains sensitive data
.env.example shows the structure without real values
Free tier of OpenWeatherMap allows 1000 requests per day
