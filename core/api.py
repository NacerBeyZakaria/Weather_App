import requests
import urllib.parse
from PyQt5.QtCore import QThread, pyqtSignal
from config.translations import WEATHER_DESCRIPTIONS

class WeatherFetchThread(QThread):
    """Background thread for fetching weather data"""
    finished = pyqtSignal(dict)
    error = pyqtSignal(str)

    def __init__(self, city_name=None, lat=None, lon=None):
        super().__init__()
        self.city_name = city_name
        self.lat = lat
        self.lon = lon

    def run(self):
        try:
            if self.lat is not None and self.lon is not None:
                city_display = "Your Location"
                country = ""
                lat = self.lat
                lon = self.lon
            else:
                
                encoded_city = urllib.parse.quote(self.city_name)
                geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={encoded_city}&count=10&format=json"

                geo_response = requests.get(geocode_url, timeout=10)
                geo_data = geo_response.json()

                if "results" not in geo_data or len(geo_data["results"]) == 0:
                    self.error.emit(f"❌ City '{self.city_name}' not found.\n\nPlease check the spelling and try again.")
                    return

                
                location = geo_data["results"][0]

                lat = location["latitude"]
                lon = location["longitude"]
                city_display = location["name"]
                country = location.get("country", "")

           
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,weathercode,precipitation_sum,precipitation_probability_max,windspeed_10m_max,relative_humidity_2m_max,sunrise,sunset,uv_index_max&hourly=temperature_2m,apparent_temperature,weathercode,precipitation_probability,windspeed_10m,relative_humidity_2m&current=temperature_2m,apparent_temperature,weathercode&timezone=auto&forecast_days=7"
            weather_response = requests.get(weather_url, timeout=10)
            weather_data = weather_response.json()

            
            aqi_data = None
            try:
                aqi_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&current=european_aqi"
                aqi_response = requests.get(aqi_url, timeout=5)
                aqi_data = aqi_response.json()
            except:
                pass

            
            alerts = []
            for i, code in enumerate(weather_data["daily"]["weathercode"]):
                if code in [65, 82, 95, 96, 99]:
                    date = weather_data["daily"]["time"][i]
                    alerts.append({
                        "date": date,
                        "code": code,
                        "description": WEATHER_DESCRIPTIONS.get(code, {}).get("en", "Severe weather")
                    })

            result = {
                "city": city_display,
                "country": country,
                "latitude": lat,
                "longitude": lon,
                "daily": weather_data["daily"],
                "hourly": weather_data["hourly"],
                "current": weather_data.get("current", {}),
                "alerts": alerts,
                "aqi": aqi_data
            }

            self.finished.emit(result)

        except requests.Timeout:
            self.error.emit("⏱️ Request timed out.\n\nPlease check your internet connection and try again.")
        except requests.RequestException as e:
            self.error.emit(f"🌐 Network error:\n\n{str(e)}")
        except Exception as e:
            self.error.emit(f"⚠️ An error occurred:\n\n{str(e)}")


class LocationFetchThread(QThread):
    """Background thread for fetching user's location"""
    finished = pyqtSignal(float, float, str)
    error = pyqtSignal(str)

    def run(self):
        try:
            services = [
                "http://ip-api.com/json/",
                "https://ipapi.co/json/",
            ]
            
            for service_url in services:
                try:
                    response = requests.get(service_url, timeout=5)
                    
                    if "ip-api.com" in service_url:
                        data = response.json()
                        if data.get("status") == "success":
                            lat = data.get("lat")
                            lon = data.get("lon")
                            city = data.get("city", "Your Location")
                            if lat and lon:
                                self.finished.emit(float(lat), float(lon), city)
                                return
                    
                    elif "ipapi.co" in service_url:
                        data = response.json()
                        lat = data.get("latitude")
                        lon = data.get("longitude")
                        city = data.get("city", "Your Location")
                        if lat and lon:
                            self.finished.emit(float(lat), float(lon), city)
                            return
                except:
                    continue
            
            self.error.emit("Could not determine your location.\n\nPlease enter a city name manually.")
                
        except Exception as e:
            self.error.emit("Location detection failed.\n\nPlease enter a city name manually.")
