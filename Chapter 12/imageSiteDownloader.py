#! python3 
# imagenesiteDownloader.py Descarga imágenes de la temática seleccionada
# desde imgur.com.

import requests, os, bs4, sys, re

def descargaImagenes(categ, numImagenes):

    """ Esta función descarga 'numImagenes' de la categoría 'categ' del
        sitio 'imgur.com'. """

    # Establece la web de descarga y la búsqueda a realizar.
    webUrl = 'https://flickr.com/search/'
    busqueda = webUrl + '?=' + categ + '&text=' + categ

    # Establece el directorio de alamacenamiento de imágenes y lo crea.
    path = os.path.abspath('descargasFlickr')
    os.makedirs(path, exist_ok=True)

    # Convierte en entero 'numImagenes'.
    numImagenes = int(numImagenes)

    # Crea el objeto 'requests' de la búsqueda.
    res = requests.get(busqueda)

    try: 
        # Comprueba el estado del objeto 'res'.
        res.raise_for_status()

        # Crea el objeto 'BeatifulSoap', selecciona las imágenes y
        # crea la expresión regex para establecer la url de la imagen.
        imgurSoup = bs4.BeautifulSoup(res.text, 'html.parser')
        imagenes = imgurSoup.select('.view.photo-list-photo-view.awake')
        url_regex = re.compile(r'url\((.+?)(_.)?\.jpg')

        # Itera sobre la lista de imágenes y abre la url de la imagen.
        for i, img in enumerate(imagenes[:numImagenes]):
            baseUrl = url_regex.search(imagenes[i].get('style')).group(1)
            imagenUrl = 'https:' + baseUrl + '_b.jpg'
            descargadas = 0

            # Crea el objeto 'requests' de la url de la imagen.
            resImagen = requests.get(imagenUrl)

            try:
                # Comprueba el estado del objeto 'resImagen'.
                resImagen.raise_for_status()

                # Abre el archivo en el directorio.
                archivoImagen = open(os.path.join(path, os.path.basename(imagenUrl)), 'wb')

                # Itera sobre el contenido de la imagen y la 
                # copia en destino por partes para limitar el uso de
                # memmoria.
                for trozo in resImagen.iter_content(100_000):
                    archivoImagen.write(trozo)
                # Cierra el archivo.
                archivoImagen.close()
                descargadas += 1

            # Informa al usuario de un error en la ejecución.
            except Exception as exc:
                print(f'Ha habido un error: {exc}')

    # Informa al usuario de un error en la ejecución.
    except Exception as exc:
        print(f'Ha habido un error: {exc}')
    
    # Devuelve el número de imágenes descargadas.
    return descargadas

# Ejecuta ek programa.
if __name__ == "__main__":

    # Pide al usuario una categoría y un número de imágenes. 
    # Llama a la función.
    categ = input('Vamos a descargar algunas imágenes de imgur.com.\n¿De qué te gustaría descargar imágenes?')
    numImagenes = input('¿Cuántas imágenes quieres descargar?')
    descargadas = descargaImagenes(categ, numImagenes)

    # Informa al usuario de la descarga realizada o de la descarga
    # realizada.
    if descargadas == 0:
        print('Vaya, no hemos podido descargar ninguna imagen.')
    else:
        print(f'Ya tienes tus {numImagenes} imágenes disponibles en "C:/Users/tu_ruta/descargasImgur"')
    pass