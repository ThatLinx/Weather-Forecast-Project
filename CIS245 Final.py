import requests, json

apiKey = "a6c36ee525113dfa0a012225959df0d9"

def main():
    #Main Variables
    stillUsing = True
    locationValid = False
    
    #Main loop
    while stillUsing is True:
        #Validation loop to make sure that selected location exists
        while locationValid is False:
            #Lines 11 to 20 get location and then convert it to Lat and Lon for accurate location information while checking whether to use Api call for zip or name
            requestedLocation = input("What city are you looking for? (Enter zip or city name and state e.g. Springfield, OR): ")
            try:
                int(requestedLocation)    
            except ValueError:
                locationUrl = f"http://api.openweathermap.org/geo/1.0/direct?q={requestedLocation.replace(' ', '')},US&appid={apiKey}"
            else:
                locationUrl = f"http://api.openweathermap.org/geo/1.0/zip?zip={requestedLocation},US&appid={apiKey}"
                
            locationResponse = requests.get(locationUrl)
            locationData = locationResponse.json()



        #Lines 25-39 check to make sure location entered is not a jumble of letters, numbers, symbols, or empty strings. It also checks to see if Zip or City name and State is being used and gets the proper url for the forecast API call
            try:
                if locationUrl == f"http://api.openweathermap.org/geo/1.0/direct?q={requestedLocation.replace(' ', '')},US&appid={apiKey}" and requestedLocation.replace(' ', '') != "":
                    forecastUrl = f"https://api.openweathermap.org/data/2.5/weather?lat={locationData[0]['lat']}&lon={locationData[0]['lon']}&appid={apiKey}"
                    
                    locationValid = True
                elif requestedLocation.replace(' ', '') != "":
                    forecastUrl = f"https://api.openweathermap.org/data/2.5/weather?lat={locationData['lat']}&lon={locationData['lon']}&appid={apiKey}"
                    
                    locationValid = True
                else:
                    print("That Location Does Not Exist")
            except IndexError:
                print("That Location Does Not Exist")
            except KeyError:
                print("That Location Does Not Exist")
            
        forecastResponse = requests.get(forecastUrl)
        forecastData = forecastResponse.json()




        print(forecastResponse)
        print(forecastData)

        print(locationResponse)
        print(locationData)
main()

def kelvinToFahrenheit(kelvin):
    fahrenheit = ((kelvin*9)/5) - 459.67
    return fahrenheit