from datetime import datetime as dt


def kelvinToFahrenheit(kelvin):
    fahrenheit = ((kelvin*9)/5) - 459.67
    return fahrenheit

def getWeather(forecastData):
    return forecastData['weather'][0]['main']

def getTemp(forecastData):
    return round(kelvinToFahrenheit(forecastData['main']['temp']), 2)

def getTempMax(forecastData):
    return round(kelvinToFahrenheit(forecastData['main']['temp_max']), 2)

def getTempMin(forecastData):
    return round(kelvinToFahrenheit(forecastData['main']['temp_min']), 2)

def getWindSpeed(forecastData):
    return forecastData['wind']['speed']

def getTime(forecastData):
    utcTime = dt.utcfromtimestamp(forecastData['dt']).strftime("%I:%M:%S%p %h-%d-%Y")
    time = dt.utcfromtimestamp(forecastData['dt']+forecastData['timezone']).strftime("%I:%M:%S%p %h-%d-%Y")
    bothTimes = f"UTC Time is: {utcTime}\nLocal Time is: {time}"
    return bothTimes