
WEATHER_ICONS = {
    0: "☀️",  # Clear sky
    1: "🌤️",  # Mainly clear
    2: "⛅",  # Partly cloudy
    3: "☁️",  # Overcast
    45: "🌫️", # Fog
    48: "🌫️", # Depositing rime fog
    51: "🌦️", # Light drizzle
    53: "🌦️", # Moderate drizzle
    55: "🌧️", # Dense drizzle
    61: "🌧️", # Slight rain
    63: "🌧️", # Moderate rain
    65: "⛈️", # Heavy rain
    71: "🌨️", # Slight snow
    73: "❄️",  # Moderate snow
    75: "❄️",  # Heavy snow
    77: "🌨️", # Snow grains
    80: "🌦️", # Slight rain showers
    81: "⛈️", # Moderate rain showers
    82: "⛈️", # Violent rain showers
    85: "🌨️", # Slight snow showers
    86: "❄️",  # Heavy snow showers
    95: "⛈️", # Thunderstorm
    96: "⛈️", # Thunderstorm with slight hail
    99: "⛈️"  # Thunderstorm with heavy hail
}

# Weather descriptions with translations (ALL LANGUAGES)
WEATHER_DESCRIPTIONS = {
    0: {"en": "Clear sky", "fr": "Ciel dégagé", "es": "Cielo despejado", "de": "Klarer Himmel", "ar": "سماء صافية"},
    1: {"en": "Mainly clear", "fr": "Plutôt dégagé", "es": "Mayormente despejado", "de": "Überwiegend klar", "ar": "صافٍ في الغالب"},
    2: {"en": "Partly cloudy", "fr": "Partiellement nuageux", "es": "Parcialmente nublado", "de": "Teilweise bewölkt", "ar": "غائم جزئياً"},
    3: {"en": "Overcast", "fr": "Couvert", "es": "Nublado", "de": "Bedeckt", "ar": "غائم"},
    45: {"en": "Foggy", "fr": "Brouillard", "es": "Niebla", "de": "Nebelig", "ar": "ضبابي"},
    48: {"en": "Depositing rime fog", "fr": "Brouillard givrant", "es": "Niebla helada", "de": "Gefrierender Nebel", "ar": "ضباب متجمد"},
    51: {"en": "Light drizzle", "fr": "Bruine légère", "es": "Llovizna ligera", "de": "Leichter Nieselregen", "ar": "رذاذ خفيف"},
    53: {"en": "Moderate drizzle", "fr": "Bruine modérée", "es": "Llovizna moderada", "de": "Mäßiger Nieselregen", "ar": "رذاذ معتدل"},
    55: {"en": "Dense drizzle", "fr": "Bruine dense", "es": "Llovizna densa", "de": "Dichter Nieselregen", "ar": "رذاذ كثيف"},
    61: {"en": "Slight rain", "fr": "Pluie légère", "es": "Lluvia ligera", "de": "Leichter Regen", "ar": "مطر خفيف"},
    63: {"en": "Moderate rain", "fr": "Pluie modérée", "es": "Lluvia moderada", "de": "Mäßiger Regen", "ar": "مطر معتدل"},
    65: {"en": "Heavy rain", "fr": "Forte pluie", "es": "Lluvia fuerte", "de": "Starker Regen", "ar": "مطر غزير"},
    71: {"en": "Slight snow", "fr": "Neige légère", "es": "Nieve ligera", "de": "Leichter Schneefall", "ar": "ثلج خفيف"},
    73: {"en": "Moderate snow", "fr": "Neige modérée", "es": "Nieve moderada", "de": "Mäßiger Schneefall", "ar": "ثلج معتدل"},
    75: {"en": "Heavy snow", "fr": "Forte neige", "es": "Nieve fuerte", "de": "Starker Schneefall", "ar": "ثلج كثيف"},
    77: {"en": "Snow grains", "fr": "Grains de neige", "es": "Granizo de nieve", "de": "Schneekörner", "ar": "حبيبات ثلجية"},
    80: {"en": "Slight rain showers", "fr": "Averses légères", "es": "Chubascos ligeros", "de": "Leichte Regenschauer", "ar": "زخات مطر خفيفة"},
    81: {"en": "Moderate rain showers", "fr": "Averses modérées", "es": "Chubascos moderados", "de": "Mäßige Regenschauer", "ar": "زخات مطر معتدلة"},
    82: {"en": "Violent rain showers", "fr": "Averses violentes", "es": "Chubascos violentos", "de": "Heftige Regenschauer", "ar": "زخات مطر عنيفة"},
    85: {"en": "Slight snow showers", "fr": "Averses de neige légères", "es": "Chubascos de nieve ligeros", "de": "Leichte Schneeschauer", "ar": "زخات ثلج خفيفة"},
    86: {"en": "Heavy snow showers", "fr": "Fortes averses de neige", "es": "Chubascos de nieve fuertes", "de": "Heftige Schneeschauer", "ar": "زخات ثلج كثيفة"},
    95: {"en": "Thunderstorm", "fr": "Orage", "es": "Tormenta", "de": "Gewitter", "ar": "عاصفة رعدية"},
    96: {"en": "Thunderstorm with hail", "fr": "Orage avec grêle", "es": "Tormenta con granizo", "de": "Gewitter mit Hagel", "ar": "عاصفة رعدية مع برَد"},
    99: {"en": "Heavy thunderstorm", "fr": "Orage violent", "es": "Tormenta fuerte", "de": "Schweres Gewitter", "ar": "عاصفة رعدية شديدة"},
}

# Weather recommendations (ALL LANGUAGES)
WEATHER_RECOMMENDATIONS = {
    0: {
        "en": "☀️ Perfect day for outdoor activities!", 
        "fr": "☀️ Journée parfaite pour les activités extérieures!", 
        "es": "☀️ ¡Día perfecto para actividades al aire libre!", 
        "de": "☀️ Perfekter Tag für Outdoor-Aktivitäten!",
        "ar": "☀️ يوم مثالي للأنشطة الخارجية!"
    },
    61: {
        "en": "☔ Take an umbrella with you", 
        "fr": "☔ Prenez un parapluie", 
        "es": "☔ Lleva un paraguas", 
        "de": "☔ Nimm einen Regenschirm mit",
        "ar": "☔ خذ مظلة معك"
    },
    63: {
        "en": "☔ Rain expected - stay dry!", 
        "fr": "☔ Pluie prévue - restez au sec!", 
        "es": "☔ Se espera lluvia - ¡mantente seco!", 
        "de": "☔ Regen erwartet - bleib trocken!",
        "ar": "☔ مطر متوقع - ابقَ جافاً!"
    },
    65: {
        "en": "⛈️ Heavy rain - avoid travel if possible", 
        "fr": "⛈️ Forte pluie - évitez de voyager", 
        "es": "⛈️ Lluvia fuerte - evita viajar", 
        "de": "⛈️ Starker Regen - vermeide Reisen",
        "ar": "⛈️ مطر غزير - تجنب السفر إن أمكن"
    },
    95: {
        "en": "⚡ Thunderstorm warning - stay indoors!", 
        "fr": "⚡ Alerte orage - restez à l'intérieur!", 
        "es": "⚡ Advertencia de tormenta - ¡quédate adentro!", 
        "de": "⚡ Gewitterwarnung - drinnen bleiben!",
        "ar": "⚡ تحذير من عاصفة رعدية - ابقَ في الداخل!"
    },
}

# AQI Categories (ALL LANGUAGES)
AQI_CATEGORIES = {
    1: {
        "label": {"en": "Good", "fr": "Bon", "es": "Bueno", "de": "Gut", "ar": "جيد"},
        "color": "#00e400",
        "advice": {"en": "Air quality is excellent", "fr": "Qualité de l'air excellente", "es": "Calidad del aire excelente", "de": "Luftqualität ist ausgezeichnet", "ar": "جودة الهواء ممتازة"}
    },
    2: {
        "label": {"en": "Fair", "fr": "Moyen", "es": "Aceptable", "de": "Mäßig", "ar": "مقبول"},
        "color": "#ffff00",
        "advice": {"en": "Air quality is acceptable", "fr": "Qualité de l'air acceptable", "es": "Calidad del aire aceptable", "de": "Luftqualität ist akzeptabel", "ar": "جودة الهواء مقبولة"}
    },
    3: {
        "label": {"en": "Moderate", "fr": "Modéré", "es": "Moderado", "de": "Befriedigend", "ar": "معتدل"},
        "color": "#ff7e00",
        "advice": {"en": "Sensitive people should reduce outdoor activity", "fr": "Personnes sensibles devraient réduire activités", "es": "Personas sensibles deben reducir actividad", "de": "Empfindliche Personen sollten Aktivitäten reduzieren", "ar": "يجب على الأشخاص الحساسين تقليل النشاط الخارجي"}
    },
    4: {
        "label": {"en": "Poor", "fr": "Mauvais", "es": "Malo", "de": "Schlecht", "ar": "سيء"},
        "color": "#ff0000",
        "advice": {"en": "Avoid prolonged outdoor activity", "fr": "Évitez activité extérieure prolongée", "es": "Evite actividad prolongada al aire libre", "de": "Längere Aktivitäten im Freien vermeiden", "ar": "تجنب النشاط الخارجي المطول"}
    },
    5: {
        "label": {"en": "Very Poor", "fr": "Très mauvais", "es": "Muy malo", "de": "Sehr schlecht", "ar": "سيء جداً"},
        "color": "#8f3f97",
        "advice": {"en": "Avoid outdoor activity - health risk", "fr": "Évitez sorties - risque santé", "es": "Evite actividad exterior - riesgo salud", "de": "Aktivitäten im Freien vermeiden - Gesundheitsrisiko", "ar": "تجنب النشاط الخارجي - خطر صحي"}
    },
}

# Language options (UPDATED)
LANGUAGES = {
    "en": "English",
    "fr": "Français",
    "es": "Español",
    "de": "Deutsch",
    "ar": "العربية"  # Added Arabic
}

# UI Translations (COMPLETE - ALL ELEMENTS)
UI_TRANSLATIONS = {
    "title": {"en": "7-Day Weather Forecast", "fr": "Prévisions météo 7 jours", "es": "Pronóstico de 7 días", "de": "7-Tage-Wettervorhersage", "ar": "توقعات الطقس لمدة 7 أيام"},
    "search_placeholder": {"en": "Enter city name", "fr": "Entrez le nom de la ville", "es": "Ingrese nombre de ciudad", "de": "Stadtname eingeben", "ar": "أدخل اسم المدينة"},
    "get_weather": {"en": "Get Weather", "fr": "Obtenir météo", "es": "Obtener clima", "de": "Wetter abrufen", "ar": "احصل على الطقس"},
    "my_location": {"en": "My Location", "fr": "Ma position", "es": "Mi ubicación", "de": "Mein Standort", "ar": "موقعي"},
    "favorites": {"en": "Favorites", "fr": "Favoris", "es": "Favoritos", "de": "Favoriten", "ar": "المفضلة"},
    "recent": {"en": "Recent", "fr": "Récent", "es": "Reciente", "de": "Letzte", "ar": "الأخيرة"},
    "add_to_favorites": {"en": "Add to Favorites", "fr": "Ajouter aux favoris", "es": "Añadir a favoritos", "de": "Zu Favoriten hinzufügen", "ar": "إضافة للمفضلة"},
    "remove_from_favorites": {"en": "Remove from Favorites", "fr": "Retirer des favoris", "es": "Quitar de favoritos", "de": "Aus Favoriten entfernen", "ar": "إزالة من المفضلة"},
    "dark_mode": {"en": "Dark Mode", "fr": "Mode sombre", "es": "Modo oscuro", "de": "Dunkler Modus", "ar": "الوضع الداكن"},
    "light_mode": {"en": "Light Mode", "fr": "Mode clair", "es": "Modo claro", "de": "Heller Modus", "ar": "الوضع الفاتح"},
    "auto_refresh_on": {"en": "Auto-refresh: ON", "fr": "Actualisation auto: OUI", "es": "Actualización auto: SÍ", "de": "Auto-Aktualisierung: AN", "ar": "التحديث التلقائي: مفعّل"},
    "auto_refresh_off": {"en": "Auto-refresh: OFF", "fr": "Actualisation auto: NON", "es": "Actualización auto: NO", "de": "Auto-Aktualisierung: AUS", "ar": "التحديث التلقائي: معطّل"},
    "sunrise": {"en": "Sunrise", "fr": "Lever du soleil", "es": "Amanecer", "de": "Sonnenaufgang", "ar": "شروق الشمس"},
    "sunset": {"en": "Sunset", "fr": "Coucher du soleil", "es": "Puesta del sol", "de": "Sonnenuntergang", "ar": "غروب الشمس"},
    "air_quality": {"en": "Air Quality", "fr": "Qualité de l'air", "es": "Calidad del aire", "de": "Luftqualität", "ar": "جودة الهواء"},
    "feels_like": {"en": "Feels like", "fr": "Ressenti", "es": "Sensación", "de": "Gefühlt", "ar": "يبدو وكأنه"},
    "humidity": {"en": "Humidity", "fr": "Humidité", "es": "Humedad", "de": "Luftfeuchtigkeit", "ar": "الرطوبة"},
    "wind": {"en": "Wind", "fr": "Vent", "es": "Viento", "de": "Wind", "ar": "الرياح"},
    "rain": {"en": "Rain", "fr": "Pluie", "es": "Lluvia", "de": "Regen", "ar": "المطر"},
    "uv": {"en": "UV", "fr": "UV", "es": "UV", "de": "UV", "ar": "الأشعة فوق البنفسجية"},
    "click_for_hourly": {"en": "Click for hourly", "fr": "Cliquer pour horaire", "es": "Clic para horario", "de": "Klicken für stündlich", "ar": "انقر للساعة"},
    "hourly_forecast": {"en": "Hourly Forecast", "fr": "Prévisions horaires", "es": "Pronóstico horario", "de": "Stündliche Vorhersage", "ar": "توقعات ساعية"},
    "precipitation_probability": {"en": "Precipitation Probability Throughout the Day", "fr": "Probabilité de précipitation tout au long de la journée", "es": "Probabilidad de precipitación durante el día", "de": "Niederschlagswahrscheinlichkeit im Tagesverlauf", "ar": "احتمالية هطول الأمطار طوال اليوم"},
    "close": {"en": "Close", "fr": "Fermer", "es": "Cerrar", "de": "Schließen", "ar": "إغلاق"},
    "loading": {"en": "Loading...", "fr": "Chargement...", "es": "Cargando...", "de": "Laden...", "ar": "جارٍ التحميل..."},
    "fetching": {"en": "Fetching weather data...", "fr": "Récupération des données météo...", "es": "Obteniendo datos del clima...", "de": "Wetterdaten werden abgerufen...", "ar": "جارٍ جلب بيانات الطقس..."},
    "error_occurred": {"en": "Error occurred. Please try again.", "fr": "Erreur survenue. Réessayez.", "es": "Ocurrió un error. Inténtelo de nuevo.", "de": "Fehler aufgetreten. Bitte erneut versuchen.", "ar": "حدث خطأ. يرجى المحاولة مرة أخرى."},
    "city_not_found": {"en": "City not found.\n\nPlease check the spelling and try again.", "fr": "Ville non trouvée.\n\nVérifiez l'orthographe et réessayez.", "es": "Ciudad no encontrada.\n\nVerifique la ortografía e inténtelo de nuevo.", "de": "Stadt nicht gefunden.\n\nBitte Schreibweise prüfen und erneut versuchen.", "ar": "المدينة غير موجودة.\n\nيرجى التحقق من الإملاء والمحاولة مرة أخرى."},
    "enter_city": {"en": "Enter a city name or use your location to see the 7-day forecast", "fr": "Entrez un nom de ville ou utilisez votre position pour voir les prévisions", "es": "Ingrese un nombre de ciudad o use su ubicación para ver el pronóstico", "de": "Geben Sie einen Stadtnamen ein oder nutzen Sie Ihren Standort", "ar": "أدخل اسم مدينة أو استخدم موقعك لرؤية التوقعات"},
    "showing_forecast": {"en": "Showing 7-day forecast for", "fr": "Affichage prévisions 7 jours pour", "es": "Mostrando pronóstico de 7 días para", "de": "7-Tage-Vorhersage für", "ar": "عرض توقعات 7 أيام لـ"},
    "weather_alerts": {"en": "WEATHER ALERTS", "fr": "ALERTES MÉTÉO", "es": "ALERTAS METEOROLÓGICAS", "de": "WETTERWARNUNGEN", "ar": "تنبيهات الطقس"},
    "locating": {"en": "Locating...", "fr": "Localisation...", "es": "Localizando...", "de": "Standortbestimmung...", "ar": "جارٍ تحديد الموقع..."},
    "detecting_location": {"en": "Detecting your location...", "fr": "Détection de votre position...", "es": "Detectando su ubicación...", "de": "Ihr Standort wird ermittelt...", "ar": "جارٍ تحديد موقعك..."},
    "none": {"en": "(none)", "fr": "(aucun)", "es": "(ninguno)", "de": "(keine)", "ar": "(لا يوجد)"},
    # Day names
    "monday": {"en": "Monday", "fr": "Lundi", "es": "Lunes", "de": "Montag", "ar": "الاثنين"},
    "tuesday": {"en": "Tuesday", "fr": "Mardi", "es": "Martes", "de": "Dienstag", "ar": "الثلاثاء"},
    "wednesday": {"en": "Wednesday", "fr": "Mercredi", "es": "Miércoles", "de": "Mittwoch", "ar": "الأربعاء"},
    "thursday": {"en": "Thursday", "fr": "Jeudi", "es": "Jueves", "de": "Donnerstag", "ar": "الخميس"},
    "friday": {"en": "Friday", "fr": "Vendredi", "es": "Viernes", "de": "Freitag", "ar": "الجمعة"},
    "saturday": {"en": "Saturday", "fr": "Samedi", "es": "Sábado", "de": "Samstag", "ar": "السبت"},
    "sunday": {"en": "Sunday", "fr": "Dimanche", "es": "Domingo", "de": "Sonntag", "ar": "الأحد"},
}

def get_translated_day_name(day_of_week_en, language):
    """Convert English day name to target language"""
    day_mapping = {
        "Monday": "monday",
        "Tuesday": "tuesday", 
        "Wednesday": "wednesday",
        "Thursday": "thursday",
        "Friday": "friday",
        "Saturday": "saturday",
        "Sunday": "sunday"
    }
    key = day_mapping.get(day_of_week_en, "monday")
    return UI_TRANSLATIONS[key][language]