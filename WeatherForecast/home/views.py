from django.shortcuts import render
from home.models import weather
from home.forms import LocationForm
import requests
import os
import json

# Create your views here.

def home(request):

    print(os.getenv('api_key'))

    if (request.method == "POST"):
        location_form = LocationForm(request.POST)
        if (location_form.is_valid()):
            cityname = location_form.cleaned_data["city"]            
    else: cityname = "London" # default

    url = "https://api.openweathermap.org/data/2.5/weather?q=" + cityname + "&appid=" + os.getenv('api_key') + "&units=imperial"
    city_weather = requests.get(url).json()
    # print(city_weather)

    temp = str(float(city_weather['main']['temp']))
    x = weather(temperature = temp, location = cityname)

    location_form = LocationForm()

    return render(request, 'home.html', {'weather':x, 'LocationForm':location_form})
