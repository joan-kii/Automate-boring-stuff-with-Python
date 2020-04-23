#!python3
# resizeAndAddLogoExtended.py Redimensiona imágenes y les añade un logo.

from PIL import Image
import os

# Establece las dimensiones de la imagen y el nombre de archivo en
# minúsculas.
DIMENSIONES_CUADRADO = 300
DIMENSIONES_CUADRADO_LOGO = 50
ARCHIVO_LOGO = 'catlogo.PNG'
ARCHIVO_LOGO = ARCHIVO_LOGO.lower()

# Abre imagen logo y establece las dimensiones.
imagenLogo = Image.open(ARCHIVO_LOGO)
logoAncho, logoAlto = imagenLogo.size

# Si las dimensiones del logo son superiores a las dimensiones
# deseadas, redimensiona el logo de forma proporcional.
if logoAncho > DIMENSIONES_CUADRADO_LOGO and logoAlto > DIMENSIONES_CUADRADO_LOGO:
        if logoAncho > logoAlto:
            logoAlto = int((DIMENSIONES_CUADRADO_LOGO / logoAncho) * logoAlto)
            logoAncho = DIMENSIONES_CUADRADO_LOGO
        else:
            logoAncho = int((DIMENSIONES_CUADRADO_LOGO / logoAlto) * logoAncho)
            logoAlto = DIMENSIONES_CUADRADO_LOGO

        print(f'Redimensionando {ARCHIVO_LOGO}...')
        imagenLogo = imagenLogo.resize((logoAncho, logoAlto))
# Si no existe, crea el directorio.
os.makedirs('conLogo', exist_ok=True)

# Comprueba los archivos de imagen en el directorio, abre cada archivo
# y establece las dimensiones.
for archivo in os.listdir('.'):
    if not (archivo.endswith('.jpg') or archivo.endswith('.png') or archivo.endswith('.gif') or archivo.endswith('.bmp')) \
         or archivo == ARCHIVO_LOGO:
        continue

    im = Image.open(archivo)
    ancho, alto = im.size
    
    # Si las dimensiones del logo son superiores a las dimensiones
    # deseadas, redimensiona el logo de forma proporcional.
    if ancho > DIMENSIONES_CUADRADO and alto > DIMENSIONES_CUADRADO:
        if ancho > alto:
            alto = int((DIMENSIONES_CUADRADO / ancho) * alto)
            ancho = DIMENSIONES_CUADRADO
        else:
            ancho = int((DIMENSIONES_CUADRADO / alto) * ancho)
            alto = DIMENSIONES_CUADRADO

        print(f'Redimensionando {archivo}...')
        im = im.resize((ancho, alto))
        # Comprueba el tamaño del logo con respecto a la imagen, y si
        # es inferior a la mitad, pega el logo en el archivo y lo guarda. 
        if (ancho / 2) < logoAncho or (alto / 2) < logoAlto:
            continue
        else:
            print(f'Añadiendo lo a {archivo}')
            im.paste(imagenLogo, (ancho - logoAncho, alto - logoAlto), imagenLogo)

            im.save(os.path.join('conLogo', archivo))