import os

import telebot

import gpt

from dotenv import load_dotenv

load_dotenv(dotenv_path='token.env')  # Cargar variables de entorno desde token.env

# Ahora puedes acceder a las variables de entorno como os.getenv('NOMBRE_VARIABLE')


BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'Saludo'])
def send_welcome(message):
    bot.reply_to(message, "Hola, Cómo estasss?")
"""
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)"""

# Manejador para comandos '/gpt' o '/ChatGPT'
@bot.message_handler(commands=['gpt', 'ChatGPT'])
def ask_chatgpt(message):
    respuesta_chatgpt = gpt.conexion_ChatGPT(message.text)  # Llamada a la función para obtener la respuesta de ChatGPT
    bot.reply_to(message, respuesta_chatgpt)


bot.infinity_polling()

