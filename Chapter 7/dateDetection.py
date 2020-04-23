#! python3
#! dateDetection.py Extrae fechas del portapapeles y detecta si son fechas correctas.

# Copia este texto en el portapapeles.
""" Jennifer López nació el 24/7/1969, la caló apretaba,
Brian McKnighte el 5/6/1969, el mismo día que yo, pero muchos años antes. 
Charlie Massó nació el 33/6/1969, (fecha inválida)
Ice Cube, Nacimiento: 15/13/1969, (fecha inválida)
Aleks Syntek nació el 29/9/1969, pff... Aleks Syntek... 
Gwen Stefani, Nacimiento: 3/10/1969, no sé quién es. 
Pelé do Nascimiento el 3/10/1940, 
Thierry Henry, Nacimiento:29/2/1977, (fecha inválida). """ 

import pyperclip, re

# Compila 1 o 2 dígitos para el día en el primer grupo.
# Detecta '/', '-' o '.' como separador. 
# Compila 1 o 2 dígitos para el mes en el segundo grupo.
# Detecta '/', '-' o '.' como separador. 
# Compila 4 dígitos para el año en el tercer grupo.
dateRegex = re.compile(r'(\d|\d\d)[\/|\-|\.](\d|\d\d)[\/|\-|\.](\d{4})')

# Pega el contenido del portapapeles como 'string'.
text = str(pyperclip.paste())

# Añade los grupos encontrados en el texto a la lista.
matches = []
for group in dateRegex.findall(text):
    matches.append(group)
# Valida las fechas según los días del mes y de año bisiesto.
fechas = []
month30 = [4, 6, 9, 11]
month31 = [1, 3, 5, 7, 8, 10, 12]
for date in matches:
    day, month, year = date
    # Si el mes tiene 30 días.
    if int(month) in month30  and int(day) > 0 and int(day) < 31:
        fechas.append(date)
    # Si el mes tiene 31 días.
    elif int(month) in month31  and int(day) > 0 and int(day) < 32:
        fechas.append(date)
    # Si el mes tiene 28 en año no bisiesto.
    elif int(month) == 2 and int(day) > 0 and int(day) < 29:
        fechas.append(date)
    # Si el mes tiene 29 días en año bisiesto.
    elif int(day) == 29 and int(month) == 2 and int(year) % 100 == 0 and int(year) % 400 == 0:
        fechas.append(date)
    else:
        continue
# No hay fechas válidas.
if fechas == []:
    print('No hemos encontrado ninguna fecha válida')
# Fechas válidas.
else:
    totalFechas = []
    for fecha in fechas:
        totalFechas.append('/'.join(fecha))

    print('Estas son las fechas que hemos encontrado: ' + ', '.join(totalFechas))
