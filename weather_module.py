"""
Weather Module for RFT Omega Bot
Provides meteorological data with RFT-aligned formatting
"""

import requests
import logging
from typing import Dict, Any
from rft_core import rft_weather_analysis, coherence_omega_obs, predict_rft_state

logger = logging.getLogger(__name__)

class WeatherProvider:
    """Weather data provider with RFT integration"""
    
    def __init__(self):
        self.api_key = "2da4fb4274e25b1aa1c60f2fa57260a5"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def fetch_weather(self, city: str) -> Dict[str, Any]:
        """
        Fetch weather data for specified city
        
        Args:
            city: City name to get weather for
            
        Returns:
            Dictionary containing weather data or error information
        """
        
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            weather_result = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "pressure": data["main"]["pressure"],
                "country": data["sys"]["country"],
                "status": "success"
            }
            
            logger.info(f"Weather data retrieved for {city}: {weather_result['temperature']}°C")
            return weather_result

        except requests.exceptions.RequestException as e:
            logger.error(f"Weather API request failed: {str(e)}")
            return {
                "status": "error",
                "message": str(e)
            }
        except KeyError as e:
            logger.error(f"Weather API response parsing error: {str(e)}")
            return {
                "status": "error",
                "message": f"Invalid response format: {str(e)}"
            }
    
    def format_weather_rft_style(self, weather_data: Dict[str, Any]) -> str:
        """
        Format weather data in RFT-aligned style with enhanced calculations
        
        Args:
            weather_data: Weather information dictionary
            
        Returns:
            RFT-formatted weather string
        """
        
        if weather_data["status"] != "success":
            return f"Weather observation failed: {weather_data.get('message', 'Unknown error')}"
        
        # Extract atmospheric parameters
        temp_celsius = weather_data["temperature"]
        humidity = weather_data["humidity"]
        pressure = weather_data["pressure"]
        wind_speed = weather_data["wind_speed"]
        
        # Perform comprehensive RFT analysis
        rft_analysis = rft_weather_analysis(temp_celsius, humidity, wind_speed, pressure)
        
        if rft_analysis is None:
            return "RFT analysis failed - using fallback display"
        
        # Extract RFT parameters
        omega_obs = rft_analysis['omega_obs']
        tau_eff = rft_analysis['tau_eff']
        delta_phi = rft_analysis['delta_phi']
        state = rft_analysis['state']
        render_factor = rft_analysis['render_factor']
        coherence_level = rft_analysis['coherence_level']
        
        formatted_weather = f"""🌤️ RFT Atmospheric Analysis

📍 Location: {weather_data['city']}, {weather_data['country']}
🌡 Conditions: {weather_data['description'].title()}

Primary Measurements:
• Temperature: {temp_celsius}°C
• Humidity: {humidity}%
• Pressure: {pressure} hPa
• Wind Velocity: {wind_speed} m/s

RFT Coherence Matrix:
• Ω_obs: {omega_obs}
• τ_eff: {tau_eff}
• Δφ: {delta_phi}
• Render Factor: {render_factor}

Observer State: {state}
Coherence Level: {coherence_level}

🔮 Atmospheric RFT Status: SYNCHRONIZED"""

        return formatted_weather
    
    def get_simple_weather_analysis(self, city: str) -> str:
        """
        Get simplified weather analysis similar to the provided format
        """
        weather_data = self.fetch_weather(city)
        
        if weather_data["status"] != "success":
            return "⚠️ Weather data not found."
        
        temp = weather_data["temperature"]
        humidity = weather_data["humidity"]
        wind_speed = weather_data["wind_speed"]
        
        # Use RFT core functions
        omega_obs = coherence_omega_obs(temp, humidity, wind_speed)
        state = predict_rft_state(omega_obs)
        
        return f"📍 {weather_data['city']}\n🌡 {temp}°C | 💧 {humidity}% | 🌬 {wind_speed}m/s\n🔮 Ω_obs = {omega_obs} → {state}"