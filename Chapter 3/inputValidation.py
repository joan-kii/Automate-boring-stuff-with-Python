#!python3
# inputValidation.py Realiza la secuencia Collatz que acaba siempre en 1. 
# Solicita al usuario que ingrese un número.

def collatz(number):
    """ Función que ejecuta la secuencia Collatz: 
    
    Si 'number' es par, divide el número por 2. Si es impar, 
    lo multiplica por 3 y le suma 1. En cada ciclo del 'loop' 
    se actualiza el valor de 'number'. El 'loop' se seguirá ejecutando
    mientras 'number' sea distinto de 1. """

    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        print(int(number))
    return int(number)

# Solicita al usuario que ingrese un número. Convierte la entrada 
# en entero, absoluto y redondea. Si salta 'Exception: ValueError'
# avisa al usuario y le pide un número.
print('Dime un número:')
while True:
    try: 
        number = round(abs(int(input())))
        break
    except ValueError:
        print('Vamos, eso no es un número. Dime un número:')

# Llama a la función 'collatz' y le pasa 'number'.
collatz(number)  
