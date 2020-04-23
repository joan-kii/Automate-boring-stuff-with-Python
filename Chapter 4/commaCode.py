#!python3
# commaCode.py Devuelve los valores de una lista separados por comas
# y la añade la conjunción 'and' entre los dos últimos.

def commaCode(myList):
    """ Función que devuelve una lista como 'string':

    Si la lista está vacía, informa al usuario.
    Si la lista solo contiene un ítem, devuelve ese ítem.
    Realiza un 'loop' sobre 'myList' excepto los dos últimos ítems,
    añadiendo a 'frase' cada ítem más ', espacio'. Añade el penúltimo
    ítem más 'espacio and espacio' más el último ítem. """

    frase = ''
    if myList == []:
        print('Lista vacía.')
    elif len(myList) == 1:
        frase = myList[0] 
    else:
        for index in range(len(myList) - 2):
            frase += myList[index] + ', ' 
        frase += myList[-2] + ' and ' + myList[-1]
    print(frase)
    return frase

# Llama a la función 'commaCode' y le pasa 'spam'.
spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'birds']
commaCode(spam)
