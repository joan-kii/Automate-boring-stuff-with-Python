#! python3
# stringPasswordDetection.py Detecta si tu contraseña es suficintemente fuerte

# Contraseñas de prueba.
""" Contraseña fuerte: jhgF657UGHf
    Contraseña débil: 1234 """

import pyperclip, re

# Detecta longitud de al menos 8 dígitos.
lengthPasswordRegex = re.compile(r'(\w{8})')
# Detecta al menos 1 número.
numberPasswordRegex = re.compile(r'(\d)')
# Detecta mayúsculas.
upperPasswordRegex = re.compile(r'([A-Z])')
# Detecta minúsculas.
lowerPasswordRegex = re.compile(r'([a-z])')

# Pega la contraseña del portapapeles.
password = pyperclip.paste()

# Comprueba si la contraseña cumple cada criterio.
lengthPassword = lengthPasswordRegex.search(password)
numberPassword = numberPasswordRegex.search(password)
upperPassword = upperPasswordRegex.search(password)
lowerPassword = lowerPasswordRegex.search(password)

# Si ninguna función devuelve 'None', la contraseña es fuerte.
if  lengthPassword != None and numberPassword != None and upperPassword != None and lowerPassword != None:
    print('Tu contraseña es muy fuerte.')
else: 
    print('Tu contraseña no es lo suficientemente fuerte.')
