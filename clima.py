import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime

log_path = Path(__file__).parent / "logs" / "registro.txt"



class Botclima:
    def __init__(self, ciudad):
        load_dotenv()
        self.apikey = os.getenv("API_KEY")
        self.url = "http://api.openweathermap.org/data/2.5/weather"
        self.ciudad = ciudad
        
    def obtener_clima(self):
        params = {
                "q": self.ciudad,
                "appid": self.apikey,
                "units": "metric",  # para obtener celsius
                "lang": "es"        # descripciones en español
            }
        
        respuesta = requests.get(self.url, params=params).json()
        
        if respuesta["cod"] != "200":
            print(f"❌ Error: {respuesta['message']}")
            return
        
        informaciom_clima = f"""
        🌤️  {respuesta["name"]}, {respuesta["sys"]["country"]}
        🌡️  Temperatura: {respuesta["main"]["temp"]}°C
        💧  Humedad: {respuesta["main"]["humidity"]}%
        💨  Viento: {respuesta["wind"]["speed"]} km/h
        🌥️  Descripción: {respuesta["weather"][0]["description"]}
        """      
        print(informaciom_clima)
        
        log_path.parent.mkdir(exist_ok=True)  # Crear carpeta logs si no existe
        with open(log_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"{datetime.now()}\n" + informaciom_clima + "\n" + "-"*40 + "\n")
        
        
        
        
if __name__ == "__main__":
    ciudad = input("¿De qué ciudad quieres saber el clima? ")
    Botclima(ciudad).obtener_clima()