import sys
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QFrame, QMessageBox, QComboBox
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

# Your modular app imports:
from config.translations import LANGUAGES, UI_TRANSLATIONS, AQI_CATEGORIES
from core.api import WeatherFetchThread, LocationFetchThread
from core.favorites import FavoritesManager
from gui.widgets import DayCard, HourlyForecastDialog
from datetime import datetime



class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.dark_mode = False 
        self.fetch_user_location_for_theme()
        self.weather_data = None
        self.favorites_manager = FavoritesManager()
        self.current_language = self.favorites_manager.get_language()
        
        self.setWindowTitle("🌤️ Modern Weather App - 7 Day Forecast")
        self.setGeometry(100, 100, 1400, 850)
        
        # Auto-refresh timer
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.auto_refresh)
        
        self.apply_theme()
        self.fetch_thread = None
        self.location_thread = None
        self.init_ui()

    def fetch_user_location_for_theme(self):
    # Use your LocationFetchThread to get lat/lon
        self.location_thread = LocationFetchThread()
        self.location_thread.finished.connect(self._set_theme_by_sun_times)
        self.location_thread.error.connect(self._fallback_local_time_theme)
        self.location_thread.start()

    def _set_theme_by_sun_times(self, lat, lon, city):
        # Use WeatherFetchThread to get daily weather for user's real location
        self.fetch_thread = WeatherFetchThread(lat=lat, lon=lon)
        self.fetch_thread.finished.connect(self._auto_theme_from_weather)
        self.fetch_thread.error.connect(self._fallback_local_time_theme)
        self.fetch_thread.start()

    def _auto_theme_from_weather(self, data):
        sunrise_str = data['daily']['sunrise'][0]
        sunset_str = data['daily']['sunset'][0]
        sunrise = datetime.strptime(sunrise_str, '%Y-%m-%dT%H:%M')
        sunset = datetime.strptime(sunset_str, '%Y-%m-%dT%H:%M')
        now = datetime.now()
        # 'now' is your computer time, and sunrise/sunset are local times.
        # So if your computer time matches your local area, this works perfectly:
        if sunrise <= now < sunset:
            self.dark_mode = False      # day = light
        else:
            self.dark_mode = True       # night = dark
        self.apply_theme()
        # Optionally, update the theme button, etc.

    def _fallback_local_time_theme(self, *args):
        now = datetime.now()
        if 7 <= now.hour < 19:
            self.dark_mode = False
        else:
            self.dark_mode = True
        self.apply_theme()
    

    def apply_theme(self):
        if self.dark_mode:
            self.setStyleSheet("""
                QWidget { background-color: #1e1e1e; font-family: Arial, sans-serif; color: #f5f5f5; }
                QLineEdit { padding: 12px; font-size: 16px; border: 2px solid #444; border-radius: 8px; background: #2d2d2d; color: #f5f5f5; }
                QLineEdit:focus { border: 2px solid #667eea; }
                QPushButton { padding: 12px 24px; font-size: 16px; font-weight: bold; border: none; border-radius: 8px; 
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #667eea, stop:1 #764ba2); color: white; }
                QPushButton:hover { background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #764ba2, stop:1 #667eea); }
                QPushButton:pressed { padding: 13px 24px 11px 24px; }
                QScrollArea { border: none; background: transparent; }
                QComboBox { padding: 8px; border: 2px solid #444; border-radius: 6px; background: #2d2d2d; color: #f5f5f5; }
            """)
        else:
            self.setStyleSheet("""
                QWidget { background-color: #f0f2f5; font-family: Arial, sans-serif; color: #333; }
                QLineEdit { padding: 12px; font-size: 16px; border: 2px solid #ddd; border-radius: 8px; background: white; color: #333; }
                QLineEdit:focus { border: 2px solid #667eea; }
                QPushButton { padding: 12px 24px; font-size: 16px; font-weight: bold; border: none; border-radius: 8px; 
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #667eea, stop:1 #764ba2); color: white; }
                QPushButton:hover { background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #764ba2, stop:1 #667eea); }
                QPushButton:pressed { padding: 13px 24px 11px 24px; }
                QScrollArea { border: none; background: transparent; }
                QComboBox { padding: 8px; border: 2px solid #ddd; border-radius: 6px; background: white; color: #333; }
            """)

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # Header with title, language selector, and theme toggle
        header_layout = QHBoxLayout()

        title_text = UI_TRANSLATIONS["title"][self.current_language]
        self.title = QLabel(f"🌤️ {title_text}")
        self.title.setFont(QFont("Arial", 24, QFont.Bold))
        self.title.setStyleSheet("color: #667eea; background: transparent;")
        header_layout.addWidget(self.title)

        
        header_layout.addStretch()
        
        # Language selector
        lang_label = QLabel("🌐")
        lang_label.setStyleSheet("background: transparent; font-size: 18px;")
        header_layout.addWidget(lang_label)
        
        self.lang_combo = QComboBox()
        for code, name in LANGUAGES.items():
            self.lang_combo.addItem(name, code)
        current_index = list(LANGUAGES.keys()).index(self.current_language)
        self.lang_combo.setCurrentIndex(current_index)
        self.lang_combo.currentIndexChanged.connect(self.change_language)
        self.lang_combo.setFixedWidth(130)
        header_layout.addWidget(self.lang_combo)
        
        # Auto-refresh toggle
        self.auto_refresh_btn = QPushButton("🔄 Auto-refresh: OFF")
        self.auto_refresh_btn.clicked.connect(self.toggle_auto_refresh)
        self.auto_refresh_btn.setCursor(Qt.PointingHandCursor)
        self.auto_refresh_btn.setFixedWidth(180)
        header_layout.addWidget(self.auto_refresh_btn)
        
        # Theme toggle
        self.theme_btn = QPushButton("🌙 Dark Mode")
        self.theme_btn.clicked.connect(self.toggle_theme)
        self.theme_btn.setCursor(Qt.PointingHandCursor)
        self.theme_btn.setFixedWidth(150)
        header_layout.addWidget(self.theme_btn)
        
        main_layout.addLayout(header_layout)

        # Input section with location button
        input_layout = QHBoxLayout()
        input_layout.setSpacing(15)
        
        loc_text = UI_TRANSLATIONS["my_location"][self.current_language]
        self.location_btn = QPushButton(f"📍 {loc_text}")
        self.location_btn.clicked.connect(self.fetch_current_location)
        self.location_btn.setCursor(Qt.PointingHandCursor)
        self.location_btn.setFixedWidth(150)
        
        placeholder_text = UI_TRANSLATIONS["search_placeholder"][self.current_language]
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText(placeholder_text)
        self.city_input.returnPressed.connect(self.fetch_weather)
        
        weather_text = UI_TRANSLATIONS["get_weather"][self.current_language]
        self.fetch_button = QPushButton(f"🔍 {weather_text}")
        self.fetch_button.clicked.connect(self.fetch_weather)
        self.fetch_button.setCursor(Qt.PointingHandCursor)

        input_layout.addWidget(self.location_btn)
        input_layout.addWidget(self.city_input, 4)
        input_layout.addWidget(self.fetch_button, 1)
        main_layout.addLayout(input_layout)

        # Favorites and Recent section
        quick_access_layout = QHBoxLayout()
        quick_access_layout.setSpacing(10)
        
        fav_text = UI_TRANSLATIONS["favorites"][self.current_language]
        self.fav_label = QLabel(f"⭐ {fav_text}:")  # Changed to self.fav_label
        self.fav_label.setFont(QFont("Arial", 11, QFont.Bold))
        self.fav_label.setStyleSheet("background: transparent;")
        quick_access_layout.addWidget(self.fav_label)
        
        self.favorites_container = QHBoxLayout()
        self.favorites_container.setSpacing(5)
        quick_access_layout.addLayout(self.favorites_container)
        
        quick_access_layout.addStretch()
        
        recent_text = UI_TRANSLATIONS["recent"][self.current_language]
        self.recent_label = QLabel(f"🕒 {recent_text}:")  # Changed to self.recent_label
        self.recent_label.setFont(QFont("Arial", 11, QFont.Bold))
        self.recent_label.setStyleSheet("background: transparent;")
        quick_access_layout.addWidget(self.recent_label)
        
        self.recent_container = QHBoxLayout()
        self.recent_container.setSpacing(5)
        quick_access_layout.addLayout(self.recent_container)
        
        main_layout.addLayout(quick_access_layout)
        
        self.update_quick_access_buttons()

        # City info, AQI, and favorite button
        city_info_layout = QHBoxLayout()
        
        self.city_label = QLabel("")
        self.city_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.city_label.setStyleSheet("background: transparent;")
        self.city_label.setAlignment(Qt.AlignCenter)
        city_info_layout.addWidget(self.city_label)
        
        # Air Quality Index
        self.aqi_label = QLabel("")
        self.aqi_label.setFont(QFont("Arial", 11, QFont.Bold))
        self.aqi_label.setStyleSheet("background: transparent; padding: 8px 16px; border-radius: 15px;")
        self.aqi_label.setVisible(False)
        city_info_layout.addWidget(self.aqi_label)
        
        self.favorite_btn = QPushButton("⭐ Add to Favorites")
        self.favorite_btn.clicked.connect(self.toggle_favorite)
        self.favorite_btn.setCursor(Qt.PointingHandCursor)
        self.favorite_btn.setVisible(False)
        self.favorite_btn.setFixedWidth(180)
        city_info_layout.addWidget(self.favorite_btn)
        
        main_layout.addLayout(city_info_layout)

        # Weather alerts banner
        self.alerts_label = QLabel("")
        self.alerts_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.alerts_label.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff6b6b, stop:1 #ee5a6f);
            color: white; padding: 12px; border-radius: 8px;
        """)
        self.alerts_label.setAlignment(Qt.AlignCenter)
        self.alerts_label.setVisible(False)
        main_layout.addWidget(self.alerts_label)

        # Scroll area for weather cards
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        self.weather_container = QWidget()
        self.weather_layout = QHBoxLayout()
        self.weather_layout.setSpacing(15)
        self.weather_container.setLayout(self.weather_layout)
        
        scroll.setWidget(self.weather_container)
        main_layout.addWidget(scroll)

        # Status label
        self.status_label = QLabel("👆 Enter a city name or use your location to see the 7-day forecast")
        self.status_label.setFont(QFont("Arial", 12))
        self.status_label.setStyleSheet("background: transparent;")
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)

        self.setLayout(main_layout)

    def change_language(self):
        self.current_language = self.lang_combo.currentData()
        self.favorites_manager.set_language(self.current_language)
        
        # Update UI text
        title_text = UI_TRANSLATIONS["title"][self.current_language]
        self.setWindowTitle(f"🌤️ {title_text}")
        
        placeholder_text = UI_TRANSLATIONS["search_placeholder"][self.current_language]
        self.city_input.setPlaceholderText(placeholder_text)
        
        weather_text = UI_TRANSLATIONS["get_weather"][self.current_language]
        self.fetch_button.setText(f"🔍 {weather_text}")
        
        loc_text = UI_TRANSLATIONS["my_location"][self.current_language]
        self.location_btn.setText(f"📍 {loc_text}")
        
        # Update auto-refresh button
        if self.refresh_timer.isActive():
            refresh_text = UI_TRANSLATIONS["auto_refresh_on"][self.current_language]
            self.auto_refresh_btn.setText(f"🔄 {refresh_text}")
        else:
            refresh_text = UI_TRANSLATIONS["auto_refresh_off"][self.current_language]
            self.auto_refresh_btn.setText(f"🔄 {refresh_text}")
        
        # Update theme button
        if self.dark_mode:
            theme_text = UI_TRANSLATIONS["light_mode"][self.current_language]
            self.theme_btn.setText(f"☀️ {theme_text}")
        else:
            theme_text = UI_TRANSLATIONS["dark_mode"][self.current_language]
            self.theme_btn.setText(f"🌙 {theme_text}")

        fav_text = UI_TRANSLATIONS["favorites"][self.current_language]
        self.fav_label.setText(f"⭐ {fav_text}:")
        
        recent_text = UI_TRANSLATIONS["recent"][self.current_language]
        self.recent_label.setText(f"🕒 {recent_text}:")

        new_title = UI_TRANSLATIONS["title"][self.current_language]
        self.title.setText(f"🌤️ {new_title}")
        self.setWindowTitle(f"🌤️ {new_title}")
        
        # **FIX: Update favorites and recent labels immediately**
        self.update_quick_access_buttons()
        # Refresh weather cards if data exists
        if self.weather_data:
            self.clear_weather_cards()
            self.display_weather(self.weather_data)

    def toggle_auto_refresh(self):
        if self.refresh_timer.isActive():
            self.refresh_timer.stop()
            refresh_text = UI_TRANSLATIONS["auto_refresh_off"][self.current_language]
            self.auto_refresh_btn.setText(f"🔄 {refresh_text}")
        else:
            self.refresh_timer.start(1800000)  # 30 minutes
            refresh_text = UI_TRANSLATIONS["auto_refresh_on"][self.current_language]
            self.auto_refresh_btn.setText(f"🔄 {refresh_text}")


    def auto_refresh(self):
        if self.city_input.text().strip():
            self.fetch_weather()

    def update_quick_access_buttons(self):
        while self.favorites_container.count():
            item = self.favorites_container.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        while self.recent_container.count():
            item = self.recent_container.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        favorites = self.favorites_manager.get_favorites()
        for fav in favorites[:5]:
            btn = QPushButton(f"{fav['city']}")
            btn.setStyleSheet("""
                QPushButton { background: #ffd700; color: #333; border: none; padding: 6px 12px; border-radius: 15px; font-size: 11px; font-weight: bold; }
                QPushButton:hover { background: #ffed4e; }
            """)
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, c=fav['city']: self.quick_search(c))
            self.favorites_container.addWidget(btn)
        
        if not favorites:
            none_text = UI_TRANSLATIONS["none"][self.current_language]
            no_fav = QLabel(none_text)
            no_fav.setStyleSheet("color: #999; font-size: 11px; background: transparent;")
            self.favorites_container.addWidget(no_fav)
        
        recent = self.favorites_manager.get_recent()
        for rec in recent[:5]:
            btn = QPushButton(f"{rec['city']}")
            btn.setStyleSheet("""
                QPushButton { background: #e0e0e0; color: #333; border: none; padding: 6px 12px; border-radius: 15px; font-size: 11px; }
                QPushButton:hover { background: #d0d0d0; }
            """)
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, c=rec['city']: self.quick_search(c))
            self.recent_container.addWidget(btn)
        
        if not recent:
            none_text = UI_TRANSLATIONS["none"][self.current_language]
            no_recent = QLabel(none_text)
            no_recent.setStyleSheet("color: #999; font-size: 11px; background: transparent;")
            self.recent_container.addWidget(no_recent)

    def quick_search(self, city):
        self.city_input.setText(city)
        self.fetch_weather()

    def toggle_theme(self):
        self._manual_theme = True
        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            theme_text = UI_TRANSLATIONS["light_mode"][self.current_language]
            self.theme_btn.setText(f"☀️ {theme_text}")
        else:
            theme_text = UI_TRANSLATIONS["dark_mode"][self.current_language]
            self.theme_btn.setText(f"🌙 {theme_text}")

        self.apply_theme()
        self.update_quick_access_buttons()


    def fetch_current_location(self):
        self.location_btn.setEnabled(False)
        self.location_btn.setText("📍 Locating...")
        self.status_label.setText("📍 Detecting your location...")
        
        self.location_thread = LocationFetchThread()
        self.location_thread.finished.connect(self.on_location_found)
        self.location_thread.error.connect(self.on_location_error)
        self.location_thread.start()

    def on_location_found(self, lat, lon, city):
        loc_text = UI_TRANSLATIONS["my_location"][self.current_language]
        self.location_btn.setEnabled(True)
        self.location_btn.setText(f"📍 {loc_text}")
        
        self.fetch_button.setEnabled(False)
        self.fetch_button.setText("⏳ Loading...")
        self.status_label.setText("🔄 Fetching weather data for your location...")
        self.city_label.setText("")
        self.clear_weather_cards()
        
        self.fetch_thread = WeatherFetchThread(lat=lat, lon=lon)
        self.fetch_thread.finished.connect(self.display_weather)
        self.fetch_thread.error.connect(self.show_error)
        self.fetch_thread.start()

    def on_location_error(self, error_msg):
        loc_text = UI_TRANSLATIONS["my_location"][self.current_language]
        self.location_btn.setEnabled(True)
        self.location_btn.setText(f"📍 {loc_text}")
        self.status_label.setText("❌ Could not detect location")
        QMessageBox.warning(self, "Location Error", error_msg)

    def fetch_weather(self):
        city = self.city_input.text().strip()
        if not city:
            QMessageBox.warning(self, "Input Error", "Please enter a city name!")
            return

        self.fetch_button.setEnabled(False)
        self.fetch_button.setText("⏳ Loading...")
        self.status_label.setText("🔄 Fetching weather data...")
        self.city_label.setText("")
        self.favorite_btn.setVisible(False)
        self.alerts_label.setVisible(False)
        self.aqi_label.setVisible(False)
        
        self.clear_weather_cards()

        self.fetch_thread = WeatherFetchThread(city)
        self.fetch_thread.finished.connect(self.display_weather)
        self.fetch_thread.error.connect(self.show_error)
        self.fetch_thread.start()

    def display_weather(self, data):

        # --- AUTO NIGHT/DAY THEME BASED ON LOCATION'S SUNRISE/SUNSET ---
        try:
            # Today's sunrise and sunset (ISO 8601 string from API)
            sunrise_str = data['daily']['sunrise'][0]
            sunset_str  = data['daily']['sunset'][0]
            sunrise = datetime.fromisoformat(sunrise_str)
            sunset = datetime.fromisoformat(sunset_str)
            now = datetime.now(sunrise.tzinfo) if sunrise.tzinfo else datetime.now()
            # Only auto-set if user hasn't toggled theme manually yet
            auto_theme = not hasattr(self, "_manual_theme") or not self._manual_theme
            if auto_theme:
                self.dark_mode = not (sunrise <= now < sunset)
                self.apply_theme()
                # update theme button text for consistency
                if self.dark_mode:
                    theme_text = UI_TRANSLATIONS["light_mode"][self.current_language]
                    self.theme_btn.setText(f"☀️ {theme_text}")
                else:
                    theme_text = UI_TRANSLATIONS["dark_mode"][self.current_language]
                    self.theme_btn.setText(f"🌙 {theme_text}")
        except Exception as e:
            pass  # fallback silently if API didn't give sunrise/sunset

        weather_text = UI_TRANSLATIONS["get_weather"][self.current_language]
        self.fetch_button.setEnabled(True)
        self.fetch_button.setText(f"🔍 {weather_text}")
        self.weather_data = data

        city = data["city"]
        country = data["country"]
        self.city_label.setText(f"📍 {city}, {country}")
        showing_text = UI_TRANSLATIONS["showing_forecast"][self.current_language]
        hourly_text = UI_TRANSLATIONS["click_for_hourly"][self.current_language]
        self.status_label.setText(f"✅ {showing_text} {city} ({hourly_text})")
        
        # Update favorite button
        self.favorite_btn.setVisible(True)
        if self.favorites_manager.is_favorite(city):
            remove_text = UI_TRANSLATIONS["remove_from_favorites"][self.current_language]
            self.favorite_btn.setText(f"💛 {remove_text}")
        else:
            add_text = UI_TRANSLATIONS["add_to_favorites"][self.current_language]
            self.favorite_btn.setText(f"⭐ {add_text}")
        
        # Display Air Quality Index
        if data.get("aqi") and data["aqi"].get("current"):
            aqi_value = data["aqi"]["current"].get("european_aqi", 0)
            if aqi_value > 0:
                # Map AQI to categories
                if aqi_value <= 20:
                    category = 1
                elif aqi_value <= 40:
                    category = 2
                elif aqi_value <= 60:
                    category = 3
                elif aqi_value <= 80:
                    category = 4
                else:
                    category = 5
                aqi_info = AQI_CATEGORIES[category]
                aqi_text = UI_TRANSLATIONS["air_quality"][self.current_language]
                aqi_label_text = aqi_info['label'][self.current_language]
                aqi_advice_text = aqi_info['advice'][self.current_language]
                self.aqi_label.setText(f"💨 {aqi_text}: {aqi_label_text} ({aqi_value}) - {aqi_advice_text}")
                self.aqi_label.setStyleSheet(f"""
                    background: {aqi_info['color']}; 
                    color: {'white' if category > 2 else 'black'};
                    padding: 8px 16px; border-radius: 15px; font-weight: bold;
                """)
                self.aqi_label.setVisible(True)
        
        self.favorites_manager.add_recent(city, country)
        self.update_quick_access_buttons()
        
        # Display weather alerts
        if data["alerts"]:
            alert_prefix = UI_TRANSLATIONS["weather_alerts"][self.current_language]
            alert_text = f"⚠️ {alert_prefix}: "
            alert_dates = [alert["date"] for alert in data["alerts"][:3]]
            alert_text += ", ".join(alert_dates)
            if len(data["alerts"]) > 3:
                alert_text += f" (+{len(data['alerts'])-3} more)"
            self.alerts_label.setText(alert_text)
            self.alerts_label.setVisible(True)
        else:
            self.alerts_label.setVisible(False)

        daily = data["daily"]
        hourly = data["hourly"]
        
        dates = daily["time"]
        temps_max = daily["temperature_2m_max"]
        temps_min = daily["temperature_2m_min"]
        weather_codes = daily["weathercode"]
        humidity = daily["relative_humidity_2m_max"]
        wind_speeds = daily["windspeed_10m_max"]
        precipitation = daily["precipitation_sum"]
        precip_prob = daily["precipitation_probability_max"]
        sunrises = daily["sunrise"]
        sunsets = daily["sunset"]
        uv_indices = daily["uv_index_max"]

        for i in range(min(7, len(dates))):
            midday_hour = i * 24 + 12
            feels_like_max = round(hourly["apparent_temperature"][midday_hour], 1) if midday_hour < len(hourly["apparent_temperature"]) else temps_max[i]
            
            card = DayCard(
                dates[i],
                round(temps_max[i], 1),
                round(temps_min[i], 1),
                feels_like_max,
                weather_codes[i],
                humidity[i],
                round(wind_speeds[i], 1),
                round(precipitation[i], 1),
                precip_prob[i],
                sunrises[i],
                sunsets[i],
                round(uv_indices[i], 1),
                self.current_language
            )
            
            hourly_data_for_day = self.get_hourly_data_for_day(hourly, i)
            card.set_hourly_data(hourly_data_for_day)
            card.clicked.connect(self.show_hourly_forecast)
            self.weather_layout.addWidget(card)

    def get_hourly_data_for_day(self, hourly, day_index):
        start_hour = day_index * 24
        end_hour = start_hour + 24
        
        return {
            "temperature": hourly["temperature_2m"][start_hour:end_hour],
            "feels_like": hourly["apparent_temperature"][start_hour:end_hour],
            "weathercode": hourly["weathercode"][start_hour:end_hour],
            "precipitation_prob": hourly["precipitation_probability"][start_hour:end_hour],
            "wind_speed": hourly["windspeed_10m"][start_hour:end_hour],
            "humidity": hourly["relative_humidity_2m"][start_hour:end_hour]
        }

    def show_hourly_forecast(self, date, hourly_data):
        dialog = HourlyForecastDialog(self, date, hourly_data, self.dark_mode, self.current_language)
        dialog.exec_()

    def toggle_favorite(self):
        if not self.weather_data:
            return
        
        city = self.weather_data["city"]
        country = self.weather_data["country"]
        
        if self.favorites_manager.is_favorite(city):
            self.favorites_manager.remove_favorite(city)
            self.favorite_btn.setText("⭐ Add to Favorites")
            QMessageBox.information(self, "Removed", f"{city} removed from favorites")
        else:
            self.favorites_manager.add_favorite(city, country)
            self.favorite_btn.setText("💛 Remove from Favorites")
            QMessageBox.information(self, "Added", f"{city} added to favorites!")
        
        self.update_quick_access_buttons()

    def show_error(self, error_msg):
        weather_text = UI_TRANSLATIONS["get_weather"][self.current_language]
        loc_text = UI_TRANSLATIONS["my_location"][self.current_language]
        
        self.fetch_button.setEnabled(True)
        self.fetch_button.setText(f"🔍 {weather_text}")
        self.location_btn.setEnabled(True)
        self.location_btn.setText(f"📍 {loc_text}")
        self.status_label.setText("❌ Error occurred. Please try again.")
        QMessageBox.critical(self, "Error", error_msg)

    def clear_weather_cards(self):
        while self.weather_layout.count():
            item = self.weather_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
