def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        print(int(number))
    return int(number)

print('Dime un número:')
while True:
    try: 
        number = round(abs(int(input())))
        break
    except ValueError:
        print('Vamos, eso no es un número. Dime un número:')
collatz(number)  
