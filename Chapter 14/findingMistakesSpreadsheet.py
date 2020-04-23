#!python3
# findingMistakesSpreadsheet.py Encuentra errores en un archivo spreadsheet.

import ezsheets

# Carga el archivo y la hoja activa.
ss = ezsheets.Spreadsheet('1TJQr3QE8EmHQ-aj-sooR-7E_rGxz7qzHcizWYIfux1w')
hoja = ss[0]

# Determina la cantidad de filas de la hoja.
hoja.rowCount =15001

# Itera por todas las filas y si el valor 'Total' es distinto del
# resultado de la multiplicaión de los valores correspondientes,
# añade el número de fila a la lista 'listaErrores'.  
listaErrores = []
for filaNum in range(2, (hoja.rowCount + 1)):
    if int(hoja.getRow(filaNum)[0]) * int(hoja.getRow(filaNum)[1]) != int(hoja.getRow(filaNum)[2]):
        listaErrores.append(filaNum)

# Imprime en pantalla los errores encontrados.
print(f"Estos son los errores encontrados en el archivo: {listaErrores}")