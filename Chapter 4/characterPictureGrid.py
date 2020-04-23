#!python3
# characterPictureGrid.py Transpone una matriz formada por listas
# enform de corazón.

heart = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Itera sobre la longitud de la primera lista creando un 'nested loop'
# (bucle anidado) en el que añade a 'myLine' el ítem con el mismo índice
# de las diferentes listas.
for b in range(len(heart[0])):
    myLine = ''
    for i in range(len(heart)):
        myLine += heart[i][b]
    print(myLine, end='\n')
