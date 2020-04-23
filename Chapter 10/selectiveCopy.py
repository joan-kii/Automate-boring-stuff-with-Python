#!python3
# selectiveCopy.py Copia archivos con una extenxión concreta a un 
# directorio nuevo.

import os, shutil

# Establece los 'path' de origen y destino.
path = 'C:\\Users\\tu_path\\archivos\\'
destPath = 'C:\\Users\\tu_path\\copias'

# Crea el directorio de destino.
os.makedirs(destPath, exist_ok=True)

# Itera por cada archivo de origen y si la extensión es '.png',
# copia el archivo en destino.
for directorio in os.walk(path):
    for archivo in directorio[2]:
        if archivo.endswith('.png'):
            source = path + archivo
            copy = shutil.copy(source, destPath)
            