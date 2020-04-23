#!python3
# regexSearch.py Busca en todos los archivos '.txt' de un directorio
# el texto que encaje con una expresión regex.

import regex as re
import os, pprint

""" Expresión Regex = r'(\d|\d\d)[\/|\-|\.](\d|\d\d)[\/|\-|\.](\d{4})' """

# Pide al usuario que introduzca una expresión regex.
regex = re.compile(input('Escribe la expresión regex para iniciar la búsqueda:'))

# Establece la variable 'path'.
path = r'C:\Users\tu_path\archivos txt'

# Itera sobre todos los directorios y archivos de 'path' en busca de 
# archivos '.txt'.
textList = []
resultado = {}
for files in os.walk(path):
    # Cambia el directorio de trabajo a 'path'.
    os.chdir(path)
    for fileText in files[2]:
        # Si el archivo es '.txt', busca coincidencias con regex y
        # las añade al diccionario de salida.
        if fileText.endswith('.txt'):
            fileReader = open(fileText, 'r', encoding='latin-1')
            text = fileReader.read()
            match = regex.findall(text)
            if match != []:
                textList.append(match)
                resultado[fileText] = match

# Crea el objeto 'PrettyPrinter' e imprime el resultado.
pp = pprint.PrettyPrinter()
pp.pprint(resultado)

