import weather
import spoti
import time
import argparse
import requests
from requests.exceptions import ConnectionError

doitQuitter = False
last = 0
URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"

def execute():
    global last
    global URL

    try:
        req = requests.get(URL)
    except ConnectionError:
        print("Echec à l'ouverture de page - Mauvais URL")
        return

    while doitQuitter == False:
        if time.time() - last > 20 :
            last = time.time()

            spoti.spotify()
            
            parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
            parser.add_argument("region", nargs="?", help="""Region to get weather for, must be available region.
                                                Default is your current location determined by your IP Address""", default="")
            # parse arguments
            args = parser.parse_args()
            region = args.region
            URL += region
            # get data
            data = weather.get_weather_data(URL)
            # print data
            print("Météo pour:", data["region"])
            print("Maintenant:", data["dayhour"])
            print(f"Température maintenant: {data['temp_now']}°C")
            print("Description:", data['weather_now'])
            print("Précipitations:", data["precipitation"])
            print("Humidité:", data["humidity"])
            print("Vent:", data["wind"])
            print("Prochains jours:")
            for dayweather in data["next_days"]:
                print("="*40, dayweather["name"], "="*40)
                print("Description:", dayweather["weather"])
                print(f"Température max: {dayweather['max_temp']}°C")
                print(f"Température min: {dayweather['min_temp']}°C")   
"""
"""        
    

if __name__ == '__main__':
    execute()
