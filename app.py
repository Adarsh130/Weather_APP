from flask import Flask, render_template, request, session
import requests
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your_secret_key_here')
API_KEY = os.getenv('WEATHER_API_KEY', 'dadc9e7803554569a89104908253107')

# Set background class based on weather condition
def get_background_class(condition_text):
    condition_text = condition_text.lower()
    if "rain" in condition_text:
        return "bg-rain"
    elif "cloud" in condition_text:
        return "bg-cloud"
    elif "sun" in condition_text or "clear" in condition_text:
        return "bg-sunny"
    elif "snow" in condition_text:
        return "bg-snow"
    elif "thunder" in condition_text:
        return "bg-thunder"
    else:
        return "bg-default"

# Get weather data from WeatherAPI
def get_weather_data(query):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={query}&days=5&aqi=no&alerts=no"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current = data['current']
        location = data['location']
        forecast_days = data['forecast']['forecastday']

        weather = {
            'city': location['name'],
            'region': location['region'],
            'country': location['country'],
            'temperature': current['temp_c'],
            'condition': current['condition']['text'],
            'icon': current['condition']['icon'],
            'feelslike': current['feelslike_c'],
            'humidity': current['humidity'],
            'wind': current['wind_kph'],
            'last_updated': current['last_updated'],
            'forecast': forecast_days,
            'bg_class': get_background_class(current['condition']['text'])
        }
        return weather
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    history = session.get('history', [])

    if request.method == 'POST':
        if 'use_location' in request.form:
            city = request.form['use_location']  # This should be lat,long from JS
        else:
            city = request.form.get('city')

        if city:
            weather = get_weather_data(city)
            if weather:
                if city not in history:
                    history.append(city)
                    session['history'] = history

    return render_template('index.html', weather=weather, history=history)

if __name__ == '__main__':
    app.run(debug=True)
