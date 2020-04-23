#!python3
# chessDictionaryValidator.py Comprueba si la disposición de las piezas
# en el tablero es correcta.

def validChessBoard(board):
    """ Esta función devuelve 'True' o 'False'.

    En los diccionarios 'pos1white', 'pos2white', 'pos1black'
    y 'pos2black' se establecen las 4 posibles disposiciones
    de las fichas. Si las posiciones de cada grupo es correcta,
    certifica la disposición del tablero como correcta """

    pos1white = {'1a': 'wtower', '1b': 'whorse', '1c': 'wbishop', '1d': 'wqueen', '1e': 'wking', '1f': 'wbishop', '1g': 'whorse', '1h': 'wtower', '2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn'}
    pos2white = {'8a': 'wtower', '8b': 'whorse', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wking', '8f': 'wbishop', '8g': 'whorse', '8h': 'wtower', '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn'}
    pos1black = {'1a': 'btower', '1b': 'bhorse', '1c': 'bbishop', '1d': 'bqueen', '1e': 'bking', '1f': 'bbishop', '1g': 'bhorse', '1h': 'btower', '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn'}
    pos2black = {'8a': 'btower', '8b': 'bhorse', '8c': 'bbishop', '8d': 'bqueen', '8e': 'bking', '8f': 'bbishop', '8g': 'bhorse', '8h': 'btower', '7a': 'bpawn', '7b': 'wpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn', '7h': 'bpawn'}
    
    # Une los diccionarios de las 4 disposiciones posibles
    # en 2 tableros posibles. 
    board1 = {**pos1white, **pos2black}
    board2 = {**pos2white, **pos1black}

    if board == board1 or board == board2:
        return True
    else: 
        return False
    
# Disposiciones a comprobar:
whites = {'1a': 'wtower', '1b': 'whorse', '1c': 'wbishop', '1d': 'wqueen', '1e': 'wking', '1f': 'wbishop', '1g': 'whorse', '1h': 'wtower', '2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn'}
blacks = {'8a': 'btower', '8b': 'bhorse', '8c': 'bbishop', '8d': 'bqueen', '8e': 'bking', '8f': 'bbishop', '8g': 'bhorse', '8h': 'btower', '7a': 'bpawn', '7b': 'wpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn', '7h': 'bpawn'}

# Une las dos disposiciones en un tablero a validar.
board = {**whites, **blacks}

# Llama a la función 'validChessBoard' y le pasa las disposiciones 
# de las fichas. Imprime el resultado.
print(validChessBoard(board))