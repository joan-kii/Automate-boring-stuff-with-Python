#! python3
# eMCb.pyw Gestor de portapapeles.

"""Funcionamiento: Pulsa 'Win + r'

    py.exe eMCb.pyw save <palabra clave> - Guarda el contenido 
        del portapales en esa palabra clave.
    py.exe eMCb.pyw <palabra clave> - Carga el contenido de la palabra
        clave en el portapapeles.
    py.exe eMCb.pyw list - Carga todas las palabras clave en el
        portapapeles.
    py.exe eMCb.pyw delete - Borra todas las palabras clave 
        y su contenido. """

import pyperclip, shelve, sys

# Crea un archivo shelve.
eMCbShelf = shelve.open('eMCb')

# Si la instrucción es 'save', guarda el contenido del portapapeles
# en la palabra clave.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    eMCbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    # Si la instrucción es 'list', pega la lista de palabras clave
    # en el portapapeles.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(eMCbShelf.keys())))
    # Si es una palabra clave, pega el contenido de esa palabra clave
    # en el portapapeles.
    elif sys.argv[1] in eMCbShelf:
        pyperclip.copy(eMCbShelf[sys.argv[1]])
    # Si la instrucción es 'delete', borra todas las palabras clave 
    # y su contenido.
    elif sys.argv[1].lower() == 'delete':
        eMCbShelf.clear()

# Cierra el archivo 'shelve'.   
eMCbShelf.close()
