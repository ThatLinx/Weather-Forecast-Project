import requests, json, os, time, sys
import finalMethods as fm
apiKey = "a6c36ee525113dfa0a012225959df0d9"

def main():
    #Main Variables
    stillUsing = True
    displayInformation = True
    requestedLocation = None
    forecastUrl = None
    locationUrl = None
    listRequestedLocation = None
    
    #Main loop
    while stillUsing is True:
        #Validation loop to make sure that selected location exists
        while forecastUrl is None:
            #Lines 19 to 33 get location checks whether to use api call for zip or location name depending on if the requested location can be casted to an int, added extra formatting for cities with multiple names and extra validation for missing state codes or zip codes that are too long or too short
            while locationUrl is None:
                requestedLocation = input("What city are you looking for? (Enter zip or city name and state e.g. Springfield, OR): ")
                listRequestedLocation = requestedLocation.split(', ')
                try:
                    int(requestedLocation)    
                except ValueError:
                    try:
                        locationUrl = f"http://api.openweathermap.org/geo/1.0/direct?q={listRequestedLocation[0].replace(' ','_')},{listRequestedLocation[1]},US&appid={apiKey}"
                    except IndexError:
                        print("Please enter a valid state")
                else:
                    if len(requestedLocation) == 5:
                        locationUrl = f"http://api.openweathermap.org/geo/1.0/zip?zip={requestedLocation},US&appid={apiKey}"
                    else:
                        print("Please enter a valid zip code.")
            
            #Checks if connection to geo api is successful    
            locationResponse = requests.get(locationUrl)
            locationData = locationResponse.json()
            try:
                locationResponse.raise_for_status()
            except:
                print(f"Connection was unsuccessful. Error code {locationResponse.status_code}: {locationData['message'].split('.', 1)[0]}")
            else:
                print(f"Connection was successful.")


        #Lines 46-57 check to make sure location entered is not a jumble of letters, numbers, symbols, or empty strings. It also checks to see if Zip or City name and State is being used, get the latitude and longitude for accurate location, and gets the proper url for the forecast API call
            try:
                if locationUrl == f"http://api.openweathermap.org/geo/1.0/zip?zip={requestedLocation},US&appid={apiKey}" and requestedLocation.replace(' ', '') != "":
                    forecastUrl = f"https://api.openweathermap.org/data/2.5/weather?lat={locationData['lat']}&lon={locationData['lon']}&appid={apiKey}"
                elif requestedLocation.replace(' ', '') != "":
                    forecastUrl = f"https://api.openweathermap.org/data/2.5/weather?lat={locationData[0]['lat']}&lon={locationData[0]['lon']}&appid={apiKey}"
                else:
                    print("That Location Does Not Exist")
            except IndexError:
                print("That Location Does Not Exist")
            except KeyError:
                print("That Location Does Not Exist")
        
        #checks if connection to weather api is successful    
        forecastResponse = requests.get(forecastUrl)
        forecastData = forecastResponse.json()
        try:
            forecastResponse.raise_for_status()
        except:
            print(f"Connection was unsuccessful. Error code {forecastResponse.status_code}: {forecastData['message'].split('.', 1)[0]}")
        else:
            print(f"Connection was successful.")


        #print(locationData)
        #print(forecastData)
        
        #Functions to get forecast info
        temp = fm.getTemp(forecastData)
        tempMax = fm.getTempMax(forecastData)
        tempMin = fm.getTempMin(forecastData)
        weather = fm.getWeather(forecastData)
        
        #Displays information with check depending on whether used city name or zip code for proper url formatting to get forecast information
        while displayInformation == True:
            desiredInfo = input("What information would you like to see? (Temp, Weather, Time): ").replace(' ', '')
            #Splits inpur into a list so that can use a for loop to iterate through options
            choiceList = desiredInfo.split(',')
            try:
                forecastUrl == f"https://api.openweathermap.org/data/2.5/weather?lat={locationData['lat']}&lon={locationData['lon']}&appid={apiKey}"
                for i in choiceList:
                    if i.capitalize() == 'Temp':
                        print(f"In {locationData['name']}:")
                        print(f"The current is {temp} Fahrenheit\nThe high is {tempMax} and the low is {tempMin}")
                    elif i.capitalize() == 'Weather':
                        print(f"In {locationData['name']}:")
                        print(f"the current weather in {locationData['name']} is {weather}")
                    elif i.capitalize() == 'Time':
                        print(f"In {locationData['name']}:")
                        print(fm.getTime(forecastData))
                    elif i.capitalize() == 'All':
                        print(f"In {locationData['name']}:")
                        print(f"The current temperature is {temp} Fahrenheit\nThe high is {tempMax} and the low is {tempMin}")
                        print(f"the current weather is {weather}")
                        print(fm.getTime(forecastData))
                    else:
                        print("That information was not available")
                        
            except:
                for i in choiceList:
                    if i.capitalize() == 'Temp':
                        print(f"In {locationData[0]['name']}:")
                        print(f"The current is {temp} Fahrenheit\nThe high is {tempMax} and the low is {tempMin}")
                    elif i.capitalize() == 'Weather':
                        print(f"In {locationData[0]['name']}:")
                        print(f"the current weather is {weather}")
                    elif i.capitalize() == 'Time':
                        print(f"In {locationData[0]['name']}:")
                        print(fm.getTime(forecastData))
                    elif i.capitalize() == 'All':
                        print(f"In {locationData[0]['name']}:")
                        print(f"The current temperature is {temp} Fahrenheit\nThe high is {tempMax} and the low is {tempMin}")
                        print(f"the current weather is {weather}")
                        print(fm.getTime(forecastData))
                    else:
                        print("That information was not available")
                        
            displayInformation = False
            
        
        stillUsing = False
main()