# Adivina el número
import random
print('Estoy pensando un número entre 1 y 20')
aleat = random.randint(1, 20)
for i in range(6):
    print('Dime un número:')
    try:
        num = int(input())
    except ValueError:
        print('Ooops... Eso no es un número.')
        continue
    if num < aleat and num > 0:
        print('Nope, te has quedado corto.' )
    elif num > aleat and num < 21:
        print('Nope, te has pasado.')
    elif num < 1 or num > 20:
        print('Así no vas a acertar. Dime un número entre 1 y 20.')
    else:
        break
if num == aleat:
    print('Olé, lo has clavado!')
else:
    print('Vaya..., mi número era ' + str(aleat) + '. Has fallado por ' + str(abs(num - aleat)) + '.')
