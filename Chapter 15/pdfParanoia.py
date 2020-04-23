#!python3
# pdfParanoia.py Encripta todos los archivos pdf de un directorio.

import PyPDF2, os, re

# Establece la ruta en la que se encuentran los archivos PDF a
# encriptar.
path = 'C:/Users/tu_path/pdfs:'

# Pide al usuario una contraseña de encripatción.
print(f'Dime una contraseña para encriptar los archivos pdf de {path}')
password = input()

# Recorre todos los directorios de 'path' en busca de archivos PDF.
for raiz in os.walk(path):
    listaArchivos = raiz[2]
    for archivo in listaArchivos:
        if archivo.endswith('.pdf'):
            # Abre cada archivo PDF.
            archivoPDF = open((f'{path}/{archivo}'), 'rb')
            # Crea los objetos 'PdfFileReader' y 'PdfFileWriter'.
            pdfReader = PyPDF2.PdfFileReader(archivoPDF)
            pdfWriter = PyPDF2.PdfFileWriter()

            # Itera por las páginas de 'pdfReader' y las almacena en
            # 'pdfWriter'. 
            for paginaNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(paginaNum))

            # Crea una expresión regex para obtener el nombre del
            # archivo.
            regEx = re.search(r'([^/*]+?).pdf?$', archivo)

            # Encripta el contenido de 'pdfWriter', abre un archivo
            # nuevo con el mismo nombre más '_encrypted', y escribe el
            # contenido de 'encrypted.pdf'.  
            pdfWriter.encrypt(password)
            encryptedPdf = open(f'{regEx.group(1)}_encrypted.pdf', 'wb')
            pdfWriter.write(encryptedPdf)
            # Cierra el archivo.
            encryptedPdf.close()

print(f'Todos los archivos pdf en {path} han sido encriptados.')