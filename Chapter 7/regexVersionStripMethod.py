#! python3
# regexVersionStripMethod.py Realiza la función .strip() con regex.

import pyperclip
import regex as re

# 'String' de prueba.
"""
           Esta frase, por ejemplo.             
pppppppppppO esta otra.pppppppppppp           
"""

def stripReg(param=None):
    """ Esta función utiliza regex para eliminar caracteres.

    Si no se le pasa ningún parámetro, elimina los espacios anteriores
    y posteriores de la 'string' almacenada en el portapapeles.
    Si recibe un carácter como parámetro, lo elimina del comienzo y el
    final de la 'string' almacenada en el portapapeles.
    """
    # Pega el contenido del portapapeles.
    theString = pyperclip.paste()

    # Si no hay parámetro, elimina espacios.
    if param == None:
        regexNew = re.compile(r'^\s+(.*)\s+$')
        stringNew = regexNew.search(theString)

    # Si hay parámetro, elimina las coincidencias.
    else:
        regexNew2 = re.compile('^\\' + re.escape(param) + '+(\\w+.*[^' + re.escape(param) + '+])\\' + re.escape(param) + '+$')
        stringNew = regexNew2.search(theString)  

    return stringNew[1]

# Llama a la función 'stripReg' con o sin parámetro de entrada.
# print(stripReg('p'))
print(stripReg())
