import requests
class WeatherAPI:
    def __init__(self,city):
        self.city=city
    def get_weather(self):
        url=f"https://wttr.in/{self.city}?format=j1"
        try:
            response=requests.get(url,timeout=5)
            if response.status_code==404:
                print("Error: City not found.")
                return
            response.raise_for_status()
            data=response.json()
            temperature=data["current_condition"][0]["temp_C"]
            condition=data["current_condition"][0]["weatherDesc"][0]["value"]
            print("Weather Report")
            print("City:",self.city)
            print("Temperature:",temperature,"°C")
            print("Condition:",condition)
        except requests.exceptions.ConnectionError:
            print("Error: Network connection failed.")
        except requests.exceptions.Timeout:
            print("Error: Request timed out.")
        except requests.exceptions.RequestException as e:
            print("Error:",e)
weather=WeatherAPI("Tiruvannamalai")
weather.get_weather()
