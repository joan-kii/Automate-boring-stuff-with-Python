#!pyhton3
# lookingBusy.py Mueve el ratón de forma imperceptible para mantener la sesión activa.

import pyautogui, time

# Infroma al usuario de la ctivación de la aplicación.
print('Movimiento automático de ratón activado. Mueve el ratón a una esquina de la pantalla para desactivarlo.')

# Mueve el ratón cada 10 segundos un píxel en diagonal. 
try:
    while True:
        time.sleep(10)
        pyautogui.move(1, 1)
        time.sleep(10)
        pyautogui.move(-1, -1)

# Informa al usuario de que ha detenido la aplicación.
except Exception:
    print('Movimiento automático de ratón desactivado.')
        
            
            
    