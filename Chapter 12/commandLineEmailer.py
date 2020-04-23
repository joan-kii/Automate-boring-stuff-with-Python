#! python3
# commandLineEmailer.py Envía un email desde 'emisor@ejemplo.com' con el texto 
# introducido en la línea de comandos.

import sys, time
from selenium import webdriver

# Obtiene el email receptor y el mensaje de la línea de comandos.
if sys.argv > 2:
    emailRec = sys.argv[1]
    mensaje = ' '.join(sys.argv[2:])
else:
    print('Introcuce una dirección de email y un mensaje.')

# Establece email emisor, contraseña y asunto.
emailEmi = 'emisor@ejemplo.com'
password = 'password'
asunto = 'Aquí tienes lo tuyo.'

# Crea el objeto 'webdriver.Chrome()'.
browser = webdriver.Chrome()

# Abre en el navegador la dirección del servicio de email e introduce
# el email del usuario. 
browser.get('https://login.live.com/login.srf?')
userElem = browser.find_element_by_id('i0116')
userElem.send_keys(emailEmi)
bttElem = browser.find_element_by_id('idSIButton9')
bttElem.click()

# Introduce el 'password' del usuario.
passwordElem = browser.find_element_by_id('i0118')
passwordElem.send_keys(password)
bttElemPass = browser.find_element_by_xpath('//*[@id="idSIButton9"]')
bttElemPass.click()

# Espera 5 segundos para cargar la web.
time.sleep(5)

# Navega a la bandeja de enetrada y pulsa 'Nuevo Mensaje'.
browser.get('https://outlook.live.com/mail/0/inbox')
bttNuevoMen = browser.find_element_by_id('id__21')
bttNuevoMen.click()

# Introduce el email del receptor.
putEmail = browser.find_element_by_class_name('ms-BasePicker-input')
putEmail.send_keys(emailRec)

# Introduce asunto.
putSub = browser.find_element_by_class_name('ms-TextField-field')
putSub.send_keys(asunto)
 
# Introduce mensaje.
putMessage = browser.find_element_by_class_name('_4utP_vaqQ3UQZH0GEBVQe')
putMessage.send_keys(mensaje)

# Pulsa enviar.
bttSend = browser.find_element_by_link_text('Enviar')
bttSend.click()

# Cierra el navegador.
browser.close()