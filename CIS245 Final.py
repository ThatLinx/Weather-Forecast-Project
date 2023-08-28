import requests, json, os, time, sys
import finalMethods as fm
apiKey = "a6c36ee525113dfa0a012225959df0d9"

def main():
    #Main Variables
    stillUsing = True
    locationValid = False
    displayInformation = True
    
    #Main loop
    while stillUsing is True:
        #Validation loop to make sure that selected location exists
        while locationValid is False:
            #Lines 15 to 25 get location and then convert it to Lat and Lon for accurate location information while checking whether to use Api call for zip or name
            requestedLocation = input("What city are you looking for? (Enter zip or city name and state e.g. Springfield, OR): ")
            try:
                int(requestedLocation)    
            except ValueError:
                locationUrl = f"http://api.openweathermap.org/geo/1.0/direct?q={requestedLocation.replace(' ', '')},US&appid={apiKey}"
            else:
                locationUrl = f"http://api.openweathermap.org/geo/1.0/zip?zip={requestedLocation},US&appid={apiKey}"
                
            locationResponse = requests.get(locationUrl)
            locationData = locationResponse.json()



        #Lines 29-44 check to make sure location entered is not a jumble of letters, numbers, symbols, or empty strings. It also checks to see if Zip or City name and State is being used and gets the proper url for the forecast API call
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




        if locationResponse.ok == True:
            print(locationResponse)
        else:
            print("Couldnt connect to webservice")
        print(locationData)
        print(forecastResponse)
        print(forecastData)
        
        temp = fm.getTemp(forecastData)
        tempMax = fm.getTempMax(forecastData)
        tempMin = fm.getTempMin(forecastData)
        weather = fm.getWeather(forecastData)
        
        
        while displayInformation == True:
            desiredInfo = input("What information would you like to see? (Temp, Weather, Time): ").replace(' ', '')
            
            choiceList = desiredInfo.split(',')
            
            for i in choiceList:
                if i.capitalize() == 'Temp':
                    print(f"The current temperature is {temp} Fahrenheit\nThe High is {tempMax} and the low is {tempMin}")
                elif i.capitalize() == 'Weather':
                    print(f"the current weather is {weather}")
                elif i.capitalize() == 'Time':
                    print(fm.getTime(forecastData))
                else:
                    print("That information was not available")
            
        
        stillUsing = False
main()