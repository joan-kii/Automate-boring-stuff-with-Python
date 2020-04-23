#!python3
# instantMessengerBot.py Envía la palabra del día de la RAE a un 
# contacto a través de whatsapp web.

import pyautogui, webbrowser, requests, bs4, time, os, pyperclip

# Establece una pausa de 1 segundo entre instrucciones.
pyautogui.PAUSE = 1

# Establece las direcciones de la RAE y de Whatsapp Web.
urlRae = 'https://dle.rae.es'
urlWhats = 'https://web.whatsapp.com/'

# Conecta con la web de la RAE y comprueba el estado.
res = requests.get(urlRae)
res.raise_for_status()

# Crea el objeto BeautifulSoup.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Selecciona la etiqueta 'p.words'.
selector = soup.select('p.words')
# Selecciona el texto del enlace. 
urlPalabra = selector[0].a.get('href')
palabra = selector[0].get_text()

# Conecta con la url de la palabra del día y comprueba el estado.
res2 = requests.get(urlRae + urlPalabra)
res2.raise_for_status()
# Crea el objeto BeautifulSoup.
soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')
# Selecciona el texto de la etiqueta 'article' y lo copia en el 
# portapapeles.
selector2 = soup2.find_all('article')[0].text
pyperclip.copy(selector2)

# Abre Whatsapp Web en el navegador.
webbrowser.open(urlWhats)
time.sleep(10)

# Busca la ventana del navegador con el título 'whatsapp'.
wA = pyautogui.getWindowsWithTitle('whatsapp')
# Pulsa tabulador.
pyautogui.write('\t')
# Escribe el nombre de contacto a culturizar y pulsa enter.
pyautogui.write('Nombre_contacto')
pyautogui.press('enter')
time.sleep(3)
# Pega el contenido del portapapeles y pusa enter.
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Fuerza el cierre del navegador.
os.system('taskkill /im chrome.exe /f 2> nul')