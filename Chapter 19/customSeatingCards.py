#!python3
# customSeatingCards.py Diseña invitaciones personalizadas.

import os
from PIL import Image, ImageFont, ImageDraw

# Abre el archivo con la lista de invitados.
with open('invitados.txt') as archivo:
    listaInvitados = archivo.readlines()
    for invitado in listaInvitados:
        # Elimina los espacios que pueda haber antes y después 
        # de la string.
        invitado = invitado.strip()
        
        # Abre el archivo con la flor.
        florImg = Image.open('flor.png')
        # Crea una imagen balnca de 288 x 360 y sistema de colores
        # RGBA.
        tarjeta = Image.new('RGBA', (288, 360), 'white')
        # Pega en 'tarjeta' la imagen de la flor de 6 x 8.
        tarjeta.paste(florImg, (6, 8), florImg)
        # Crea una imagen negra de 292 x 364 y sistema de colores
        # RGBA
        borde = Image.new('RGBA', (292, 364), 'black')
        # Pega en 'tarjeta' en 'borde'.
        borde.paste(tarjeta, (2, 2))

        # Crea un objeto 'ImageDraw' con 'borde'.
        drawObj = ImageDraw.Draw(borde)
        # Establece la ruta de acceso a las fuentes de Windows.
        directFuente = r'C:\Windows\Fonts'
        # Obtiene la fuente d Windows. En este caso, 'Allegro.ttf'
        # en tamaño 22.
        fuente = ImageFont.truetype(os.path.join(directFuente, 'Allegro.ttf'), 22)
        # Establece el punto de inserción.
        punto = 100 - (len(invitado) // 2)
        # Añade el texto a la imagen creada en negro y con 
        # la fuente escogida.
        drawObj.text((punto, 170), invitado, fill='black', font=fuente)

        # Si no existe crea el directorio y guarda la imagen con el 
        # nombre de invitado
        os.makedirs('Tarjetas Invitados', exist_ok=True)
        borde.save(os.path.join('Tarjetas Invitados', f'tarjeta_{invitado}.png'))

        # Al abrir los archivos en el contexto 'with' no es necesario
        # cerrar los archivos.
        