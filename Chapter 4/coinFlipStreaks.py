#!python3
# coinFlipStreaks.py Detecta secuencias de 6 'caras' o 'cruces'
# en 10.000 tandas de 100 lanzamientos de moneda.

# Importa módulo 'random' (aleatorio).
import random

# Realiza un 'loop' de 10.000 repeticiones. Devuelve el resultado en %.
numberOfStreaks = 0
for experimentNumber in range(10_000):
    myList = []
    for flip in range(100):
        myList.append(random.randint(0, 1))

    for index in range(len(myList) - 5):
        if myList[index] == myList[index + 1] == myList[index + 2] == myList[index + 3] == myList[index + 4] == myList[index + 5]:
            numberOfStreaks += 1

print(f'Probabilidad de "streak": {numberOfStreaks / 10_000}%')
