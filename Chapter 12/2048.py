#!python3
# 2048.py Un programa que juega automáticamente a 2048.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Crea el objeto 'webdriver.Chrome()'.
browser = webdriver.Chrome()

# Abre la web en el navegador.
browser.get('https://gabrielecirulli.github.io/2048/')

# Espera 3 segundos para cargar la web.
time.sleep(3)

# Busca el elemento sobre el que actuar.
htmlElem = browser.find_element_by_tag_name('html')
time.sleep(2)

# Juega.
while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)