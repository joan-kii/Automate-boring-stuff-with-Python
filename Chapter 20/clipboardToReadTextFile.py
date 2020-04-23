#!python3
# clipboardToReadTextFile.py Cpioa en el portapapeles el contenido de 
# un archivo de texto de forma automática.

import pyperclip, pyautogui

# Establece una pausa de medio segundo entre instrucciones.
pyautogui.PAUSE = 0.5
# Busca la ventana con el título 'Blos de Notas'.
ventanaBloc = pyautogui.getWindowsWithTitle('Bloc de notas')[0]
# Obtiene la posición de la ventana.
ventanaPos = ventanaBloc.topleft
# Activa la ventana.
ventanaBloc.activate()

# Hace click encima del texto.
pyautogui.click((ventanaPos[0] + 100), (ventanaPos[1] + 100))
# Selecciona todo el contenido.
pyautogui.hotkey('ctrl', 'a')
# Copia el contenido en el portapapeles.
pyautogui.hotkey('ctrl', 'c')
# Pega el contenido y lo imprime en pantalla. 
print(pyperclip.paste())