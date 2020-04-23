#!python3
# scheduledWebComicDownloader.py Descerga los cómics de una web de cómics de forma automática.

import requests, bs4, os, datetime

# Elige la web desde la que se van a realzar las descargas.
url = 'http://xkcd.com'
# Crea el directorio si no esxiste.
os.makedirs('Cómics', exist_ok=True)

# Evita las 'urls' que acaban en '#'.
if not url.endswith('#'):
    print(f'Cargando la página {url}')
    # Descaraga la página y comprueba el estado.
    res = requests.get(url, verify=True)
    res.raise_for_status()

    # Busca el elemento etiquetado como '#comic img'.
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')
    # Informa al usuario si no ha podido realizar la descarga.
    if comicElem == []:
        print('No se ha podido encontrar ningún cómic.')

    # Crea la 'url' del cómic y si no se encuentra en el directorio,
    # descarga la imagen. 
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        if os.path.basename(comicUrl) not in os.listdir(r'C:\Users\tu_path\Cómics'):
            print(f'Descargando imagen: {comicUrl}')
            res = requests.get(comicUrl, verify=True)
            res.raise_for_status()

            # Abre el archivo en el directorio con la url como nombre.
            archivoImagen = open(os.path.join('Cómics', os.path.basename(comicUrl)), 'wb')
            # Itera por el contenido de la imagen dividiéndolo en
            # trozos y los escribe en el archivo de destino para evitar
            # la sobrecarga de memoria. 
            for chunk in res.iter_content(100000):
                archivoImagen.write(chunk)
            # Cierra el archivo e informa al usuario.
            archivoImagen.close()
            print('Hecho.')
        else:
            print('No hay ningún cómic nuevo.')

