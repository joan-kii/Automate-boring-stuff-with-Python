#!python3
# tablePrinter.py Crea una tabla a partir de una lista de listas con
# cada columna justificada a la derecha.

def tablePrinter(myList):
    """ Esta función encuentra el ancho máximo de cada columna. 
    
    Imprime una lista de listas en forma de tabla"""
    
    # Crea una lista del ancho de cada columna.
    colsWidth = [0] * len(myList)
    width = 0

    # Itera sobre cada elemento de la lista de listas y establece el 
    # ancho máximo de cada columna.
    for x in range(len(myList[0])):
        for y in range(len(myList)):
            if len(myList[y][x]) > width:
                width = len(myList[y][x])
            colsWidth[y] = width

    # Crea número de columnas y filas en función de la lista 'myList'.
    numCols = len(myList)
    numRows= len(myList[0])

    # Itera sobre el número de fila y de columna e imprime cada item
    # justificado a la derecha y con ancho columna 'colsWidth'.
    for row in range(numRows):
        for col in range(numCols):
            print(myList[col][row].rjust(colsWidth[col]), end=' ') 
        print()
        
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# Llama a la función 'tablePrinter' y le pasa 'tableData'.
tablePrinter(tableData)