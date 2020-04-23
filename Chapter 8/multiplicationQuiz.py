#! python3
# multiplicationQuiz.py Crea un uestionario de 10 preguntas 
# sobre las tablas de multiplicar.

import pyinputplus as pyip 
import random, time

try:
    # Crea un bucle infinito.

    while True:
        numPre = 10
        respCorr = 0
        print('¿Te sabes las tablas de multiplicar?\nVamos a verlo...\n')
        time.sleep(3)
        inicio = time.time()

        # Crea un 'loop' de 10 iteraciones. Elige dos númerios aleatorios
        # y muestra la operación en pantalla.
        for preg in range(numPre):
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
            prompt = f'#{preg}: {num1} x {num2} = \n'

            # Permite ingresar la respuesta corrcta. Todo lo demás
            # es incorrecto. Tiempo: 10 seg. Límite de respuestas: 3.
            try:
                pyip.inputStr(prompt, allowRegexes=[f'^{(num1 * num2)}$'],
                                                    blockRegexes=[('.*', '¡Incorrecto!')],
                                                    timeout=10, limit=3)

            # Imprime los avisos.                                       
            except pyip.TimeoutException:
                print('¡Se acabó el tiempo!\n')
            except pyip.RetryLimitException:
                print('¡No tienes más intentos!\n')
            else:
                print('¡Correcto!\n')
                respCorr += 1
                time.sleep(1)

        # Imprime el resultado de la prueba.
        print(f'Resultado: {respCorr}/{numPre}\n')
        fin = time.time()
        if respCorr >= 5:
            print(f'Enhorabuena campeona!!! Has aprobado!!!\nTiempo: {round((fin - inicio), 2)} segundos.\n')
        else:
            print('Vaya, parece que tienes que practicar las tablas un poquito más...\n')
        print('Pulsa "Ctrl-c para abandonar. Si quieres continuar, espera.\n')
        time.sleep(5)
        
except KeyboardInterrupt:
    print('\nPrueba detenida.\n')
    time.sleep(2)