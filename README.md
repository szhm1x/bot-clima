# Bot Clima 🌤️

App de Python que obtiene información del clima en tiempo real de cualquier ciudad del mundo.

## Requisitos
- Python 3.14+
- requests
- python-dotenv

## Instalación
```bash
pip install requests python-dotenv
```

## Configuración
Crea un archivo `.env` con tu API key de OpenWeatherMap:
```
API_KEY=tu_api_key_aqui
```

## Uso
```bash
python clima.py
```
Ingresa el nombre de la ciudad y listo ✅

## Ejemplo
```
🌤️  Santo Domingo, DO
🌡️  Temperatura: 29°C
💧  Humedad: 78%
💨  Viento: 15 km/h
🌥️  Descripción: Parcialmente nublado
```

## Logs
Cada consulta queda registrada en `logs/registro.txt` con fecha y hora.