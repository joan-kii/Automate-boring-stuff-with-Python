#!python3
# debuggingCointirada.py Adivina! ¿Cara o cruz?

import random, logging

# Configuración de 'logging.DEBUG' y de logging.'INFO'.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Deshabilita 'logging.DEBUG' y de logging.'INFO'.
logging.disable(logging.DEBUG)
logging.disable(logging.INFO) 

# Solicita al usuario que escriba 'cara' o 'cruz' y lo compara con 
# una selección aleatoria para determinar si ha acertado o no.
logging.debug('Inicio programa.\n')
prediccion = ''
while prediccion not in ('cara', 'cruz'):
    # Convierte la entrada a 'lowercase' para evitar errores
    # con las mayúsculas.
    print('¡Adivina! ¿cara o cruz?\n')
    prediccion = input().lower()
    logging.info(f'Input = {prediccion}\n')

# En lugar de elegir entre 0 y 1 (int) como propone el ejecicio, 
# elige entre 'cara' o 'cruz' (str), para poder comparar con el 
# tipo de dato que devuelve 'input()'.
tirada = random.choice(['cara', 'cruz']) 
if tirada == prediccion:
    print('\n¡Acertaste!\n')
else:
    print('\nNo. Has fallado. Inténtalo de nuevo.\n')
    # Convierte la entrada a 'lowercase' para evitar errores
    # con las mayúsculas. Aquí hay un error en el ejercicio,
    # ya que pone 'guesss' en lugar de 'guess'.
    prediccion = input().lower()
    logging.info(f'Input = {prediccion}\n')
    if tirada == prediccion:
        print('\n¡Acertaste!\n')
    else:
        print('\nNo. Eres verdaderamente malo en este juego.\n')
logging.debug('Fin programa.')