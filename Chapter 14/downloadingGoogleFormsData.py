#!python3
# googleFormsStreadsheet.py Importa datos de Google Forms.

import ezsheets

# Abre el archivo con los datos de Google Forms.
archivoGoogle = '1FAIpQLSeVhyvKN4wL8CbVXvXhSKEpeZF6RJ352pf4V8fVd7Yr94xIlA'
ss = ezsheets.Spreadsheet(archivoGoogle)
hoja = ss[0]

# Itera por las filas del archivo y copia el valor de las celdas
# de la columna 'C' en las que se encuentran las direcciones de 
# email, en la lista 'emailList'.
emailList = []
for filaNum in range(2, hoja.columnCount + 1):
    emailList.append(hoja[f'C{filaNum}'])
print(emailList)