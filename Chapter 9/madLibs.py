#!python3
# madLibs.py Lee un texto y pide al usuario que substituya las palabras clave
# ADJETIVO, ADVERBIO, SUSTANTIVO y VERBO.

""" Texto: 

El panda ADJETIVO caminó hacia el SUSTANTIVO y VERBO. A un SUSTANTIVO cercano no le afectaban estos eventos.
"""

# Abre el archivo con el texto a completar.
archivo = 'el archivo que quieras'
textFile = open(archivo, 'r', encoding='utf-8')
texto = textFile.read().split()
print(f'Esta es la frase que vamos a completar:\n{" ".join(texto)}\n')

# Itera sobre la lista 'texto' y busca las 'strings' que contienen
# un punto y separa la palabra del punto.
for index, item in enumerate(texto):
    if item.endswith('.') and item != '.':
        nuevaPalabra = item.replace('.', '')
        texto.remove(item)
        texto.insert(index, nuevaPalabra)
        texto.insert((index + 1), '.')

# Añade las palabras sugeridas por el usuario para sustituir a las
# palabras clave.
nuevoTexto = []
for palabra in texto:
    if palabra == 'ADJETIVO':
        nuevoTexto.append(input('Dime un adjetivo:\n'))
    elif palabra == 'ADVERBIO':
        nuevoTexto.append(input('Dime un adverbio:\n'))
    elif palabra == 'SUSTANTIVO':
        nuevoTexto.append(input('Dime un sustantivo:\n'))
    elif palabra == 'VERBO':
        nuevoTexto.append(input('Dime un verbo en pasado:\n'))
    else:
        nuevoTexto.append(palabra)

# Vuelve a unir los puntos a sus correspondientes palabras.
for index, item in enumerate(nuevoTexto):
    if item is ('.'):
        nuevoTexto[(index - 1)] += '.'
        nuevoTexto.remove(item)

# Crea el nuevo archivo con el nuevo texto.
newTextFile = open('Texto Completado.txt', 'w', encoding='utf-8')
newTextFile.write(' '.join(nuevoTexto))
print(' '.join(nuevoTexto))

# Cierra los dos archivos abiertos.
newTextFile.close()
textFile.close()