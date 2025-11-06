from datetime import datetime
from PyQt5.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QLabel,
    QDialog, QGridLayout, QScrollArea, QPushButton,
    QProgressBar, QWidget
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
from config.translations import (
    WEATHER_ICONS, WEATHER_DESCRIPTIONS,
    WEATHER_RECOMMENDATIONS, UI_TRANSLATIONS,
    get_translated_day_name
)

class HourlyForecastDialog(QDialog):
    """Dialog showing 24-hour forecast for a specific day"""
    def __init__(self, parent, date, hourly_data, dark_mode=False, language="en"):
        super().__init__(parent)
        self.dark_mode = dark_mode
        self.language = language
        self.setup_ui(date, hourly_data)

    def setup_ui(self, date, hourly_data):
        hourly_text = UI_TRANSLATIONS["hourly_forecast"][self.language]
        self.setWindowTitle(f"{hourly_text} - {date}")
        self.setGeometry(200, 100, 1100, 650)
        
        if self.dark_mode:
            self.setStyleSheet("""
                QDialog { background-color: #1e1e1e; color: #f5f5f5; }
                QLabel { color: #f5f5f5; }
                QFrame { background-color: #2d2d2d; border: 1px solid #444; border-radius: 8px; }
                QPushButton { background-color: #667eea; color: white; border: none; padding: 10px 20px; border-radius: 6px; font-weight: bold; }
                QPushButton:hover { background-color: #764ba2; }
            """)
        else:
            self.setStyleSheet("""
                QDialog { background-color: #f0f2f5; color: #333; }
                QLabel { color: #333; }
                QFrame { background-color: white; border: 1px solid #ddd; border-radius: 8px; }
                QPushButton { background-color: #667eea; color: white; border: none; padding: 10px 20px; border-radius: 6px; font-weight: bold; }
                QPushButton:hover { background-color: #764ba2; }
            """)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        hourly_text = UI_TRANSLATIONS["hourly_forecast"][self.language]
        title = QLabel(f"📅 {hourly_text} - {date}")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Precipitation probability graph
        precip_frame = QFrame()
        precip_layout = QVBoxLayout()
        precip_text = UI_TRANSLATIONS["precipitation_probability"][self.language]
        precip_label = QLabel(f"📊 {precip_text}")
        precip_label.setFont(QFont("Arial", 12, QFont.Bold))
        precip_label.setAlignment(Qt.AlignCenter)
        precip_layout.addWidget(precip_label)
        
        # Simple bar chart
        bars_layout = QHBoxLayout()
        for hour in range(0, 24, 3):  # Show every 3 hours
            bar_container = QVBoxLayout()
            bar_container.setSpacing(2)
            
            prob = hourly_data["precipitation_prob"][hour]
            bar = QProgressBar()
            bar.setOrientation(Qt.Vertical)
            bar.setMaximum(100)
            bar.setValue(prob)
            bar.setTextVisible(False)
            bar.setFixedSize(30, 80)
            bar.setStyleSheet(f"""
                QProgressBar {{
                    border: 1px solid #ccc;
                    border-radius: 3px;
                    background: #f0f0f0;
                }}
                QProgressBar::chunk {{
                    background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 #4facfe, stop:1 #00f2fe);
                    border-radius: 3px;
                }}
            """)
            
            hour_label = QLabel(f"{hour:02d}:00")
            hour_label.setFont(QFont("Arial", 9))
            hour_label.setAlignment(Qt.AlignCenter)
            
            prob_label = QLabel(f"{prob}%")
            prob_label.setFont(QFont("Arial", 9, QFont.Bold))
            prob_label.setAlignment(Qt.AlignCenter)
            
            bar_container.addWidget(prob_label)
            bar_container.addWidget(bar)
            bar_container.addWidget(hour_label)
            bars_layout.addLayout(bar_container)
        
        precip_layout.addLayout(bars_layout)
        precip_frame.setLayout(precip_layout)
        layout.addWidget(precip_frame)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; }")

        container = QWidget()
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        for hour in range(24):
            hour_frame = QFrame()
            hour_frame.setFrameStyle(QFrame.Box)
            
            hour_layout = QVBoxLayout()
            hour_layout.setSpacing(5)
            hour_layout.setContentsMargins(10, 10, 10, 10)

            time_label = QLabel(f"{hour:02d}:00")
            time_label.setFont(QFont("Arial", 12, QFont.Bold))
            time_label.setAlignment(Qt.AlignCenter)
            hour_layout.addWidget(time_label)

            weather_code = hourly_data["weathercode"][hour]
            icon = WEATHER_ICONS.get(weather_code, "🌤️")
            icon_label = QLabel(icon)
            icon_label.setFont(QFont("Arial", 24))
            icon_label.setAlignment(Qt.AlignCenter)
            hour_layout.addWidget(icon_label)

            desc = WEATHER_DESCRIPTIONS.get(weather_code, {}).get(self.language, "Unknown")
            desc_label = QLabel(desc)
            desc_label.setFont(QFont("Arial", 9))
            desc_label.setAlignment(Qt.AlignCenter)
            desc_label.setWordWrap(True)
            hour_layout.addWidget(desc_label)

            temp = round(hourly_data["temperature"][hour], 1)
            temp_label = QLabel(f"🌡️ {temp}°C")
            temp_label.setFont(QFont("Arial", 11, QFont.Bold))
            temp_label.setAlignment(Qt.AlignCenter)
            hour_layout.addWidget(temp_label)

            feels_like = round(hourly_data["feels_like"][hour], 1)
            feels_text = UI_TRANSLATIONS["feels_like"][self.language]
            feels_label = QLabel(f"{feels_text}: {feels_like}°C")
            feels_label.setFont(QFont("Arial", 9, QFont.StyleItalic))
            feels_label.setAlignment(Qt.AlignCenter)
            hour_layout.addWidget(feels_label)

            humidity = hourly_data["humidity"][hour]
            wind = round(hourly_data["wind_speed"][hour], 1)
            precip_prob = hourly_data["precipitation_prob"][hour]
            
            info_label = QLabel(f"💧 {humidity}%\n🌬️ {wind} km/h\n🌧️ {precip_prob}%")
            info_label.setFont(QFont("Arial", 9))
            info_label.setAlignment(Qt.AlignCenter)
            hour_layout.addWidget(info_label)

            hour_frame.setLayout(hour_layout)
            
            row = hour // 4
            col = hour % 4
            grid_layout.addWidget(hour_frame, row, col)

        container.setLayout(grid_layout)
        scroll.setWidget(container)
        layout.addWidget(scroll)

        close_text = UI_TRANSLATIONS["close"][self.language]
        close_btn = QPushButton(close_text)
        close_btn.clicked.connect(self.close)
        close_btn.setCursor(Qt.PointingHandCursor)
        layout.addWidget(close_btn)

        self.setLayout(layout)


class DayCard(QFrame):
    """Widget for displaying one day's weather"""
    clicked = pyqtSignal(str, dict)

    def __init__(self, date, temp_max, temp_min, feels_like_max, weather_code, humidity, wind_speed, precipitation, precip_prob, sunrise, sunset, uv_index, language="en"):
        super().__init__()
        self.date = date
        self.hourly_data = None
        self.language = language
        self.setup_ui(date, temp_max, temp_min, feels_like_max, weather_code, humidity, wind_speed, precipitation, precip_prob, sunrise, sunset, uv_index)
        self.setCursor(Qt.PointingHandCursor)

    def setup_ui(self, date, temp_max, temp_min, feels_like_max, weather_code, humidity, wind_speed, precipitation, precip_prob, sunrise, sunset, uv_index):
        self.setFrameStyle(QFrame.Box | QFrame.Raised)
        self.setLineWidth(2)
        
        # Dynamic backgrounds based on weather
        weather_backgrounds = {
            0: "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #56CCF2, stop:1 #2F80ED)",  # Clear - blue
            1: "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2)",  # Mainly clear
            2: "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #a8edea, stop:1 #fed6e3)",  # Partly cloudy
            3: "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #636363, stop:1 #a2ab58)",  # Overcast
            45: "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #bdc3c7, stop:1 #2c3e50)",  # Fog
            61: "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #4facfe, stop:1 #00f2fe)",  # Rain
            63: "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #43e97b, stop:1 #38f9d7)",  # Moderate rain
            65: "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #30cfd0, stop:1 #330867)",  # Heavy rain - dark
            71: "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #e0eafc, stop:1 #cfdef3)",  # Snow
            95: "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ff6b6b, stop:1 #ee5a6f)",  # Thunderstorm - red
        }
        
        background = weather_backgrounds.get(weather_code, "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2)")
        
        self.setStyleSheet(f"""
            QFrame {{
                background: {background};
                border-radius: 15px;
                padding: 20px;
                margin: 5px;
            }}
            QFrame:hover {{
                border: 3px solid white;
            }}
            QLabel {{
                color: white;
                background: transparent;
            }}
        """)

        layout = QVBoxLayout()
        layout.setSpacing(8)

        dt = datetime.strptime(date, "%Y-%m-%d")
        day_of_week_en = dt.strftime("%A")
        day_of_week = get_translated_day_name(day_of_week_en, self.language)

        
        date_label = QLabel(f"{day_of_week}\n{date}")
        date_label.setFont(QFont("Arial", 12, QFont.Bold))
        date_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(date_label)

        icon = WEATHER_ICONS.get(weather_code, "🌤️")
        icon_label = QLabel(icon)
        icon_label.setFont(QFont("Arial", 42))
        icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(icon_label)

        temp_label = QLabel(f"{temp_max}°C / {temp_min}°C")
        temp_label.setFont(QFont("Arial", 14, QFont.Bold))
        temp_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(temp_label)

        feels_text = UI_TRANSLATIONS["feels_like"][self.language]
        feels_label = QLabel(f"{feels_text}: {feels_like_max}°C")

        feels_label.setFont(QFont("Arial", 9, QFont.StyleItalic))
        feels_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(feels_label)

        # Sunrise/Sunset times
        sunrise_time = datetime.fromisoformat(sunrise).strftime("%H:%M")
        sunset_time = datetime.fromisoformat(sunset).strftime("%H:%M")
        sun_label = QLabel(f"🌅 {sunrise_time}  🌇 {sunset_time}")
        sun_label.setFont(QFont("Arial", 9))
        sun_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(sun_label)

        humidity_text = UI_TRANSLATIONS["humidity"][self.language]
        wind_text = UI_TRANSLATIONS["wind"][self.language]
        rain_text = UI_TRANSLATIONS["rain"][self.language]
        uv_text = UI_TRANSLATIONS["uv"][self.language]
        details = f"💧 {humidity_text}: {humidity}%\n🌬️ {wind_text}: {wind_speed} km/h\n🌧️ {rain_text}: {precipitation} mm ({precip_prob}%)\n☀️ {uv_text}: {uv_index}"

        details_label = QLabel(details)
        details_label.setFont(QFont("Arial", 9))
        details_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(details_label)

        # Weather recommendation
        recommendation = WEATHER_RECOMMENDATIONS.get(weather_code, {}).get(self.language, "")
        if recommendation:
            rec_label = QLabel(recommendation)
            rec_label.setFont(QFont("Arial", 8, QFont.StyleItalic))
            rec_label.setAlignment(Qt.AlignCenter)
            rec_label.setWordWrap(True)
            layout.addWidget(rec_label)

        hint_text = UI_TRANSLATIONS["click_for_hourly"][self.language]
        hint_label = QLabel(f"👆 {hint_text}")

        hint_label.setFont(QFont("Arial", 8, QFont.StyleItalic))
        hint_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(hint_label)

        self.setLayout(layout)

    def set_hourly_data(self, hourly_data):
        self.hourly_data = hourly_data

    def mousePressEvent(self, event):
        if self.hourly_data:
            self.clicked.emit(self.date, self.hourly_data)
        super().mousePressEvent(event)