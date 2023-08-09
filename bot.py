import os

import telebot

import gpt

from dotenv import load_dotenv

load_dotenv(dotenv_path='token.env')  # Cargar variables de entorno desde token.env

# Ahora puedes acceder a las variables de entorno como os.getenv('NOMBRE_VARIABLE')


BOT_TOKEN = os.environ.get('BOT_TOKEN') # Obtener el token del bot desde las variables de entorno

bot = telebot.TeleBot(BOT_TOKEN) # Crear una instancia del bot

# Manejador para el comando /start
@bot.message_handler(commands=['start'])
def send_menu(message):
    # Enviar un menú con opciones
    menu_text = "¡Bienvenido! Por favor, elige una opción:\n" \
                "/UNRaf - Enlace al sitio web de UNRaf\n" \
                "/SIU - Enlace al SIU Guarani\n" \
                "/ChatGPT - Permite ingresar una pregunta que será contestada por ChatGPT\n" \
                "/Bienvenida - Saludo"
    
    bot.send_message(message.chat.id, menu_text)

# Manejador para el comando /start o /Saludo
@bot.message_handler(commands=['Bienvenida', 'Saludo'])
def send_welcome(message):
    # Responder al mensaje con un saludo
    bot.reply_to(message, "Hola, Cómo estasss?")

"""@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)"""

# Manejador para el comando /unraf o /web
@bot.message_handler(commands=['unraf', 'UNRaf', 'web'])
def unraf_link(message):
    # Responder al mensaje con un enlace a la página de UNRAF
    bot.send_message(message.chat.id, "https://www.unraf.edu.ar/" ) 

# Manejador para el comando /SIU o /SIUGuarani
@bot.message_handler(commands=['SIU', 'siu', 'SIUGuarani'])
def unraf_link(message):
    # Responder al mensaje con un enlace al sistema SIU Guarani
    bot.send_message(message.chat.id, "https://guarani.unraf.edu.ar/autogestion/acceso")      

# Manejador para el comando '/gpt' o '/ChatGPT'
@bot.message_handler(commands=['gpt', 'ChatGPT'])
def ask_chatgpt(message):
     # Obtener la respuesta de ChatGPT utilizando la función gpt.conexion_ChatGPT
    respuesta_chatgpt = gpt.conexion_ChatGPT(message.text)  # Llamada a la función para obtener la respuesta de ChatGPT
    # Responder al mensaje con la respuesta de ChatGPT
    bot.reply_to(message, respuesta_chatgpt)

# Iniciar el ciclo de escucha del bot
bot.infinity_polling()

