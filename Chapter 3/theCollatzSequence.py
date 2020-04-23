#!python3
# theCollatzSequence.py Realiza la secuencia Collatz que acaba siempre en 1.

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
# en entero, absoluto y redondea.
print('Dime un número:')
number = round(abs(int(input())))

# Llama a la función 'collatz' y le pasa 'number'.
collatz(number)  
