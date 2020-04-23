#!python3
# umbrellaReminder.py Aviso de lluvia con la API de opneweathermap.org.

APPID = '_ID _de_acceso_API_'

import requests, smtplib, json, sys

# Establece email, lugar, idioma y url.
email = 'pirlo@ejemplo.com'
lugar = 'Marbella,es'
idioma = 'es'
url = f'https://api.openweathermap.org/data/2.5/weather?q={lugar}&APPID={APPID}&lang={idioma}'

# Carga la página y compruebe el estado.
response = requests.get(url)
response.raise_for_status()

# Convierte la predicción de 'json' a diccionario.
weatherData = json.loads(response.text)
w = weatherData['weather']
description = w[0]['description']

# Si hay aviso de lluvia en la predicción, se conecta al servidor
# de outlook y se registra con el password introducido en la línea de
# comandos. 
if 'rain' in weatherData:
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('levandoski@outlook.com', sys.argv[1])

    # Establece el mensaje y envía el email.
    mensaje = f"Subject: Parece que va a llover.\n\nQuerido Andrea,\nParece que va a llover. Coge el paraguas, anda.\nPrevision: {description}\nGracias."
    sendEmailStatus = smtpObj.sendmail('levandoski@outlook.com', email, mensaje)
    # Informa al usuario si ha habido un error en el envío.
    if sendEmailStatus != {}:
        print(f'Ha habido un problema al enviar el email a {email}: {sendEmailStatus}')