#!python3
# photoFoldersInHardDrive.py Encuentra direcorios con archivos de imagenes.

from PIL import Image
import os

# Establece la ruta de acceso al directorio a comprobar.
PATH = r'C:\Users\tu_path'

# Recorre todos los directorios, subdirectorios y archivos de la ruta 
# indicada e itera sobre los archivos.
for directorios, subdirectorios, archivos in os.walk(PATH):
    listaDirecFotos = []
    numArchivosFoto = 0
    numArchivosNoFoto = 0
    for archivo in archivos:
        # Cuenta los archivos no son una imagen.
        if not archivo.lower().endswith('.jpg') or archivo.lower().endswith('.png') or archivo.lower().endswith('.gif') or archivo.lower().endswith('.bmp'):
            numArchivosNoFoto += 1
            continue
        # Cambia el directorio de trabajo para abrir los archivos.
        os.chdir(PATH)
        # Abre el archivo. Si las dimensiones son superiores a 
        # 500 x 500, cuenta el archivo como foto. En caso contrario,
        # lo cuenta como no foto. 
        with Image.open(archivo) as im:
            ancho, alto = im.size
            if ancho > 500 or alto > 500:
                numArchivosFoto +=1
            else:
                numArchivosNoFoto += 1
            # Si más de la mitad de los archivos del directorio, son 
            # fotos, lo cuenta como directorio de fotos.
            if numArchivosFoto >= ((numArchivosFoto + numArchivosNoFoto) / 2):
                print(f'Esta es una carpeta de fotos: {os.path.abspath(archivo)}')
                listaDirecFotos.append(os.path.abspath(archivo))
            # Al abrir los archivos en el contexto 'with' no es necesario
            # cerrar el archivo.