#!python3
# fillingTheGapsChallenge.py Encuentra una serie de archivos 
# y los renombra creando brechas.

import os, random
import regex as re

# Expresión regex: - grupo 1: palabra
#                  - grupo 2: número  
#                  - grupo 3: extenxión
regex = re.compile(r'(lomio)(\d+)(.txt)')

# Itera sobre todos los archivos para encontrar las coincidencias
# y establecer la cantidad de números que formarán el nombre del 
# archivo.
longitud = 0
# En este caso los archivos se encuentran el el directorio de trabajo.
for archivo in os.listdir():
    match = regex.search(archivo)
    if match != None: 
        if len(match.group(2)) > longitud:
            longitud = len(match.group(2))

# Itera sobre todos los archivos para encontrar las coincidencias
# y cambia el nombre de los archivos teniendo en cuenta la logitud
# del número y la cantidad de '0' que debe poner.
inicio = 1
aleat = random.randint(1, 2)
for archivo in os.listdir():
    match = regex.search(archivo)
    if match != None:
        num = match.group(2)
        ceros = longitud - len(str(inicio))
        if num != inicio:
            # Inserta brechas de forma aletoria. Si el archivo ya existe
            # le suma 1 antes de crearlo.
            try:
                nuevoNombre = match.group(1) + ('0' * ceros) + str(inicio) + match.group(3)
                inicio += aleat
                os.rename(archivo, nuevoNombre)
            except FileExistsError:
                inicio += aleat + 1