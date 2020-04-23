#!python3
#convertingSpreadsheetsOtherFormats.py Convierte spreadsheets a otros formatos.

import ezsheets

def convertidor(archivo, formato):
    """ Esta función convierte un archivo spredsheet a un formato
        específico: '.xlsx', '.ods', '.csv', '.tsv', '.pdf'
        o '.html'. """
    # Carga el archivo.    
    ss = ezsheets.upload(archivo)

    # Comprueba el formato de salida y realiza la descarga.
    if formato == 'excel':
        ss.downloadAsExcel()
    elif formato == 'openoffice':
        ss.downloadAsODS()
    elif formato == 'csv':
        ss.downloadAsCSV()
    elif formato == 'tsv':
        ss.downloadAsTSV()
    elif formato == 'pdf':
        ss.downloadAsPDF()
    elif formato == 'html':
        ss.downloadAsHTML()
    else:
        print('Elige un formatoo válido: excel, openoffice, csv, tsv, pdf o html.')

# LLama a la función y le pasa el archivo a convertir y el formato
# de salida.
convertidor('produceSales.xlsx', 'pdf')
