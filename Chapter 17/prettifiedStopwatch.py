#!python3
#prettifiedStopwatch.py Pues eso, un stopwatch.

import time, pyperclip

# Informa al usuario del funcioanmeinto del cronómetro.
print('\nPulsa ENTER para comenzar. Después, pulsa ENTER de nuevo para parar el reloj en cada vuelta. Para salir, pulsa Ctrl + C.')

# Con la entrada del usuario inicia la cuenta.
input()
print('¡Vamos!')
tiempoInicio = time.time()
ultimoTiempo = tiempoInicio
numVuelta = 1

# Con cada entrada del usuario actualiza el timpo por vuelta,
# el tiempo total y el número de vuelta. 
try:
    while True:
        input()
        # Redondea a 2 decimales.
        tiempoVuelta = round(time.time() - ultimoTiempo, 2)
        tiempoTotal = round(time.time() - tiempoInicio, 2)
        # Justifica a izquierda y derecha respectivamente.
        numVueltaStr = str(numVuelta).ljust(2)
        tiempoVueltaStr = str(tiempoVuelta).rjust(5)
        tiempoTotalStr = str(tiempoTotal).rjust(5)
        # Imprime en pantalla número de vueltas y tiempos.
        print((f'Lap # {numVueltaStr}: {tiempoVueltaStr} ({tiempoTotalStr})'), end='')
        numVuelta += 1
        ultimoTiempo = time.time()
        # Copia en el portapapeles el tiempo total.
        pyperclip.copy(round(tiempoTotal, 2)) 

# Detiene el cronómetro.
except KeyboardInterrupt:
    print('\n¡Fin!\n')