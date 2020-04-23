#!python3
# listToDictFantasyGameInventory.py Añade los artículos de una lista
# al diccionario.

def displayInventory(inventory):
    """ Esta función suma los valores de un diccionario."""

    print('Inventario:')
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + ' ' + k)
    print('Número total de artículos: ' + str(item_total))

def addToInventory(inventory, addedItems):
    """ Esta función añade los items de una lista a un diccionario.

    Si el ítem no existe en el diccionario, establece el valor de cada
    'key' a 1 por defecto."""

    # Itera sobre los artículos a añadir, y si existen en el inventario,
    # suma 1 a 'value'. Si no existe lo crea con un valor de 1.
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.setdefault(i, 1)
    return inventory
    
inv = {'Moneda de Oro': 42, 'Cuerda': 1}
dragonLoot = ['Moneda de Oro', 'Daga', 'Moneda de Oro', 'Moneda de Oro', 'Rubí']

# En 'newInv' obtiene el resultado de la función 'addToInventory' 
# pasándole el diccionario 'inv' y la lista 'dragonLoot'    
newInv = addToInventory(inv, dragonLoot)

# Llama a la función 'displayInventory' y le pasa el diccionario 'newInv'.
displayInventory(newInv)
