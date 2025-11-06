import json
from pathlib import Path

class FavoritesManager:
    """Manages favorite cities and recent searches"""
    def __init__(self):
        self.config_file = Path.home() / ".weather_app_config.json"
        self.data = self.load_data()

    def load_data(self):
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {"favorites": [], "recent": [], "language": "en"}

    def save_data(self):
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")

    def add_favorite(self, city, country):
        city_data = {"city": city, "country": country}
        self.data["favorites"] = [f for f in self.data["favorites"] if f["city"] != city]
        self.data["favorites"].insert(0, city_data)
        self.data["favorites"] = self.data["favorites"][:10]
        self.save_data()

    def remove_favorite(self, city):
        self.data["favorites"] = [f for f in self.data["favorites"] if f["city"] != city]
        self.save_data()

    def is_favorite(self, city):
        return any(f["city"] == city for f in self.data["favorites"])

    def get_favorites(self):
        return self.data["favorites"]

    def add_recent(self, city, country):
        city_data = {"city": city, "country": country}
        self.data["recent"] = [r for r in self.data["recent"] if r["city"] != city]
        self.data["recent"].insert(0, city_data)
        self.data["recent"] = self.data["recent"][:5]
        self.save_data()

    def get_recent(self):
        return self.data["recent"]
    
    def set_language(self, lang):
        self.data["language"] = lang
        self.save_data()
    
    def get_language(self):
        return self.data.get("language", "en")