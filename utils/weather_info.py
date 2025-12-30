# import requests

# class WeatherForecastTool:
#     def __init__(self, api_key:str):
#         self.api_key = api_key
#         self.base_url = "https://api.openweathermap.org/data/2.5"

#     def get_current_weather(self, place:str):
#         """Get current weather of a place"""
#         try:
#             url = f"{self.base_url}/weather"
#             params = {
#                 "q": place,
#                 "appid": self.api_key,
#             }
#             response = requests.get(url, params=params)
#             return response.json() if response.status_code == 200 else {}
#         except Exception as e:
#             raise e
    
#     def get_forecast_weather(self, place:str):
#         """Get weather forecast of a place"""
#         try:
#             url = f"{self.base_url}/forecast"
#             params = {
#                 "q": place,
#                 "appid": self.api_key,
#                 "cnt": 10,
#                 "units": "metric"
#             }
#             response = requests.get(url, params=params)
#             return response.json() if response.status_code == 200 else {}
#         except Exception as e:
#             raise e



import requests

class WeatherForecastTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org"
    
    def geocode_place(self, place: str):
        """Convert place name to latitude and longitude"""
        try:
            url = f"{self.base_url}/geo/1.0/direct"
            params = {
                "q": place,
                "limit": 1,
                "appid": self.api_key
            }
            response = requests.get(url, params=params)

            if response.status_code != 200 or not response.json():
                return {}

            data = response.json()[0]
            return {
                "lat": data["lat"],
                "lon": data["lon"]
            }
        except Exception as e:
            raise e

    def get_current_weather_by_coordinates(self, lat: float, lon: float):
        """Get current weather using latitude and longitude"""
        try:
            url = f"{self.base_url}/data/2.5/weather"
            params = {
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": "metric"
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise e

    def get_forecast_weather_by_coordinates(self, lat: float, lon: float):
        """Get weather forecast using latitude and longitude"""
        try:
            url = f"{self.base_url}/data/2.5/forecast"
            params = {
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": "metric",
                "cnt": 10
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise e
