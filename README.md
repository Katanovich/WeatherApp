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
   git clone https://github.com/Katanovich/WeatherApp.git
   cd WeatherApp

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
CITY: City name (e.g., "Seoul")
UNITS: Temperature units ("metric" for Celsius, "imperial" for Fahrenheit)

USAGE python main.py
python: can't open file '/Users/katana/main.py': [Errno 2] No such file or directory

# Expected output:

# Welcome to Weather App!

✓ Configuration loaded successfully!
App Name: Weather App
API_KEY loaded: True
City: Seoul
Units: metric

==================================================
Weather in Seoul, KR
==================================================
Temperature: 15°C (feels like 14°C)
Humidity: 65%
Description: Partly cloudy
==================================================

Environment Variables
Create .env file with:

API_KEY - Your OpenWeatherMap API key (required)
API_URL - Weather API endpoint (optional, default provided)
CITY - City name to fetch weather for (optional, Seoul)
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
=========================================================

🎯 CHECKLIST: PROJECT LIFECYCLE

1. mkdir → Create folder
2. cd → Navigate to folder
3. git init → Initialize Git
4. python3 -m venv venv → Create virtual environment
5. source venv/bin/activate → Activate environment
6. pip install packages → Install packages
7. pip freeze > requirements.txt → Save dependencies
8. Create files (.gitignore, main.py, etc.)
9. git add . → Add files
10. git commit -m "message" → Save changes
11. Repeat steps 8-10 for each stage (3+ times)
12. git remote add origin URL → Connect GitHub
13. git push -u origin main → Upload to GitHub
