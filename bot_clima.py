# Importar las bibliotecas necesarias
import discord  # Biblioteca para trabajar con la API de Discord
from discord.ext import commands  # Módulo para comandos del bot
import requests  # Biblioteca para hacer solicitudes HTTP
import pyttsx3  # Biblioteca para síntesis de voz

# Inicializar el sintetizador de voz
engine = pyttsx3.init()  # Crear un objeto para la síntesis de voz

# Inicializar el objeto del bot
intents = discord.Intents.default()  # Configurar permisos para el bot
intents.message_content = True  # Habilitar la capacidad de leer el contenido
bot = commands.Bot(command_prefix="!", intents=intents)  # Prefijo signo


# Función para obtener el clima a través de la API wttr.in
def get_weather(city: str) -> str:
    """
    Obtiene datos del clima para la ciudad especificada.

    Parámetros:
        city (str): Nombre de la ciudad

    Retorna:
        str: Información del clima o mensaje de error
    """
    base_url = f"https://wttr.in/{city}?format=%C+%t"  # URL de solicitud
    response = requests.get(base_url)  # Realizar una solicitud GET a la API
    if response.status_code == 200:  # Si la solicitud es exitosa (código 200)
        return response.text.strip()  # Retornar la respuesta en texto sin espa
    else:
        return "No se pudo obtener la información del clima."  # Error menjs


# Función para la síntesis de voz
def speak(text: str):
    """
    Convierte el texto en voz usando pyttsx3.

    Parámetros:
        text (str): Texto a vocalizar
    """
    engine.say(text)  # Pasar el texto para la síntesis
    engine.runAndWait()  # Ejecutar la síntesis de voz y esperar a que termine


# Comando para obtener el clima
@bot.command()
async def weather(ctx, *, city: str):
    """
    Comando para obtener información del clima y vocalizarla.

    Parámetros:
        ctx: Contexto del comando (información sobre la ejecución del comando)
        city (str): Nombre de la ciudad
    """
    weather_info = get_weather(city)  # Obtener los datos del clima
    await ctx.send(f"Clima de la {city}: {weather_info}")  # Enviar la infor a DB
    speak(weather_info)  # Vocalizar la información obtenida


# Iniciar el bot
bot.run("Token")  # Iniciar el bot con el token
