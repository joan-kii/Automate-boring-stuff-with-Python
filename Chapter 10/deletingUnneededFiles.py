#!python3
# deletingUnneededFiles.py Imprime los archivos de más de 100MB de un 
# directorio y la ruta completa.

import os

# Esrablece la ruta a comprobar.
path = 'C:\\Users\\tu_path\\a_comprobar\\archivos_>_100MB'

# Itera por los directorios y archivo e imprime el nombre del archivo
# y su ruta completa.
for directorio, subdirectorio, archivos in os.walk(path):
    for archivo in archivos:
        pathArchivo = os.path.join(directorio, archivo)
        if os.path.getsize(pathArchivo) > 100_000_000:
            print(f'El archivo {archivo} de la ruta {os.path.abspath(pathArchivo)} tiene más de 100MB.')