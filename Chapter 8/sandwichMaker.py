#! python3
# sandwichMaker.py Házte un sándwich con pyinputplus.

import pyinputplus as pyip

""" Pide al usuario que introduzca las respuestas. """

# El propio autor recomienda no usar 'customPompt' en '.inputMenu()'.
# Pudes leerlo aquí: 
# https://www.reddit.com/r/inventwithpython/comments/e5dpux/how_to_get_pyinputplusinputmenu_to_accept_a_prompt/

# Diferentes tipos de pan.
panTipo = ['Pan Blanco', 'Pan de Espelta', 'Pan con Cereales']
promptPan = '\nElige un tipo de pan:\n'

pan = pyip.inputMenu(panTipo, numbered=True)

# Diferentes tipos de proteína animal.
proteinTipo = ['Pavo', 'Pollo', 'Atún', 'Vegetariano']
promptProtein = '\nElige el ingrediente principal:\n'

protein = pyip.inputMenu(proteinTipo, numbered=True)

# ¿Queso?
quieresQueso = '¿Quieres queso? s/n\n'
queso = pyip.inputYesNo(quieresQueso, yesVal='si', noVal='no')

if queso == 'si':
    quesoTipo = ['Cheddar', 'Mozzarella', 'Ricotta', 'Suizo']
    promptQueso = 'Elige el tipo de queso: \n'
    quesoSand = pyip.inputMenu(quesoTipo, numbered=True)

# Complementos.
quieresComplementos = '¿Quieres mayonesa, lechuga, tomate y mostaza? s/n\n'
complementos = pyip.inputYesNo(quieresComplementos, yesVal='si', noVal='no')

# Unidades.
cuantosSand = '¿Cuantos sándwiches quieres?: \n'
numSand = pyip.inputInt(cuantosSand, min=1)

# Imprime en pantalla el resúmen del pedido.
print(f'\nResumen del pedido: \n\nNúmero de sándwiches: {numSand}\nTipo de pan: {pan}\nIngrediente principal: {protein}')
if queso == 'si':
    print(f'Tipo de queso: {quesoSand}')

if complementos == 'si':
    print(f'Con mayonesa, lechuga, tomate y mostaza.\n')
