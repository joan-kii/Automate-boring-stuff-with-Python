#!python3
# pdfPasswordBreaker.py Desencripta un archivo pdf encriptado por medio de la fuerza bruta.

import PyPDF2

def passwordBreaker(archivo, diccionario):

    """ Esta función itera sobre una lista de palabras e intenta abrir
        un archivo encriptado con cada una de ellas. Si lo consigue,
        imprime la contraseña. """

    # Abre el documento que contiene el diccionario.
    diccPal = open(diccionario, 'r')
    # Crea una lista con las palabras del documento.
    listaPalabras = diccPal.readlines()

    # Abre el archivo a desencriptar.
    pdfFile = open(archivo, 'rb')
    # Crea el objeto 'PdfReader'.
    pdfReader = PyPDF2.PdfFileReader(pdfFile)

    # Itera sobre la lista de palabras e intenta desencriptar el archivo
    # tanto en mayúsculas como en minúsculas.
    conseguido = 0
    for palabra in listaPalabras:
        conseguidoMayus = pdfReader.decrypt(palabra.strip())
        conseguidoMinus = pdfReader.decrypt(palabra.lower().strip())

        # Informa al usuario si ha conseguido desencriptar el archivo
        # y la contraseña.
        if conseguidoMayus == 1:
            PASSWORD = palabra.strip()
            conseguido = 1
            print(f'Puedes desencriptar el archivo {archivo} con la contraseña: {PASSWORD}.')
            break
        elif conseguidoMinus == 1:
            password = palabra.lower().strip()
            conseguido = 1
            print(f'Puedes desencriptar el archivo {archivo} con la contraseña: {password}.')
            break

        else:
            continue
    
    # Cierra los archivos.
    diccPal.close()
    pdfFile.close()
    
    return conseguido

# Establece los archivos.
archivo= 'allminutes_encrypted.pdf'
diccionario = 'dictionary.txt'

# Llama a la función y le pasa los archivos.
logrado = passwordBreaker(archivo, diccionario)
# Informa al usuario si no ha podido desencriptar el documento.
if logrado == 0:
    print(f'No hemos podido desencriptar el archivo {archivo}.')