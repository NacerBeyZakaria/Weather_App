# Weather App

**Modern 7-Day Weather Forecast Application**  
_Powered by Open-Meteo API and PyQt5 · Multilingual · Auto-Theming · .exe Release_

---

## 🌦️ Description

Weather App is a next-generation cross-platform desktop application for effortless 7-day weather forecasts with a modern, responsive, and feature-rich interface. View detailed daily/hourly data, live air quality, save your favorite cities, and enjoy seamless theme auto-switching at sunrise/sunset based on your real location.

---

## 🚀 Features

- **7-Day Weather Forecast:**  
  Displays temperature, “feels like,” humidity, wind, rain, UV, sunrise, and sunset for each day.

- **Hourly View:**  
  Click any day for a dialog with 24-hour temperature, icons, rain probability, and weather codes.

- **Smart Theming:**  
  - **Auto-detects** if it’s night/day at your true location & picks dark/light accordingly.
  - **Manual override** with a modern toggle switch.

- **Live Air Quality Index (AQI):**  
  Instant air health updates for all locations.

- **Favorites**  
  Add any city for 1-click forecasting; unlimited favorites.

- **Recent Searches**  
  Return to previous queries instantly.

- **Multilingual Support**  
  English, French, Spanish, German, Arabic—with easy extension.

- **Auto-Refresh**  
  Toggle for periodic background weather updates.

- **Sleek, Modern UI**  
  - Flat colors, gradients, custom weather icons.
  - Highly responsive layout for any display.

- **Offline Persistence**  
  Favorites and recents remain for future launches.

- **Cross-platform**  
  - Run as Python: Windows, Linux, MacOS  
  - Distributable: One-click `.exe` with custom icon for Windows

---

## 🛠️ Installation

### As a Python App

pip install -r requirements.txt
python main.py

text
*(_or install manually: `pip install pyqt5 requests`_)  

### As a Standalone Windows App

1. Download the `.exe` from releases or build it using PyInstaller (see below).
2. Double-click `Weather App.exe`.
3. No install required.

#### To Package Yourself

pyinstaller --onefile --windowed --icon=weather.ico --name "Weather App" main.py

text

---

## ⚡ How to Use

- **My Location:**  
  Click "📍 My Location" to instantly forecast your actual position.

- **Search:**  
  Enter a city name, click "Get Weather"—supports all scripts.

- **Favorites/Recents:**  
  Add any city to favorites, or revisit recent searches via quick buttons.

- **Hourly:**  
  Click any day card (“Click for hourly”) to review in-depth 24-hour data.

- **Theme & Language:**  
  Use the toggles to shift themes or switch UI language on the fly.

- **Auto Theme:**  
  At launch, the app determines if it’s currently sunny or dark at your position, and picks the matching theme.

---

## 🗂️ Project Layout

Weather App/
├── main.py
├── weather.ico
├── config/
├── core/
├── gui/
├── dist/
├── README.md

text

---

## 💡 Customize

- **Add languages**: Edit/add `UI_TRANSLATIONS` keys in `config/translations.py`
- **Change theming**: Edit logic in `WeatherApp`.
- **Package**: See PyInstaller usage above.

---

## 📋 Credits

- Weather & AQI from [Open-Meteo API](https://open-meteo.com/)
- Custom icons (see / provide credit as needed)
- UI: PyQt5, Python 3.x
