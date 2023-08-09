import openai

# Función para conectarse a ChatGPT y obtener respuesta
def conexion_ChatGPT(pregunta):
    openai.api_key = ""  #Ver  de cambiar la API key
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=pregunta,
        max_tokens=50  # Limitar la longitud de la respuesta generada
    )
    respuesta_chatgpt = completion.choices[0].text.strip()
    return respuesta_chatgpt
