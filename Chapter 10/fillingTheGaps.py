#!python3
# fillingTheGaps.py Encuentra brechas en el nombre de una serie 
# de archivos y los renombra de forma correlativa.

import os
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
for archivo in os.listdir():
    match = regex.search(archivo)
    if match != None:
        num = match.group(2)
        ceros = longitud - len(inicio)
        if num != inicio:
            nuevoNombre = match.group(1) + ('0' * ceros) + str(inicio) + match.group(3)
            inicio += 1
            os.rename(archivo, nuevoNombre)
            


