#!python3
# fantasyGameInventory.py Muestra el inventario y el número total
# de artículos.

def displayInventory(inventory):
    """ Esta función suma los valores de un diccionario."""

    print('Inventario:')
    item_total = 0

    # Itera sobre los items del diccionario 'inventory' obteniendo
    # cada 'key' y cada 'value'. En 'item_total' suma todos los 'value'.
    for k, v in inventory.items():
        item_total += v
        print(str(v) + ' ' + k)
    print('Número total de artículos: ' + str(item_total))

stuff = {'Cuerda': 1, 'Antorcha': 6, 'Moneda de Oro': 42, 'Daga': 1, 'Flecha': 12}
# Llama a la función 'displayInventory' y pasa el diccionario 'stuff'.
displayInventory(stuff)