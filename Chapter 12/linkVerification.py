#!python3
# linkVerification.py Comprueba el estado de los enlaces de una web.

import requests, bs4

def verificador(url):
    """ Esta función realiza un 'scrapping' de una web y comprueba
        estado de los 'links'. """

    # Crea el objeto 'requests' de la url. 
    res = requests.get(url)

    try:
        # Comprueba el estado del objeto 'res'.
        res.raise_for_status()

        # Crea el onjeto 'BeautitfulSoap.
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Crea una lista con todos lo links de la web.
        listaLinks = []
        for link in soup.select('a'):
            listaLinks.append(link.get('href'))

        linkRoto = 0
        linkCorrecto = 0

        # Itera sobre la lista de links y los abre para comprobar
        # el estado.
        for linkF in listaLinks:
            if linkF.startswith('http'):
                # Crea el objeto 'requests' del link.
                resL = requests.get(linkF)

                try:
                # Comprueba el estado del objeto 'resL' y lo cuenta
                # como correcto o incorrecto.
                    resL.raise_for_status()
                    print(f'Enlace correcto: {linkF}')
                    linkCorrecto += 1

                except Exception as exc:
                    print(f'Enlace roto: {linkF}')
                    linkRoto += 1
        # Informa al usuario de la cantidad de enlaces rotos
        # y correctos.
        print(f'Enlaces correctos: {linkCorrecto}.\nEnlaces rotos: {linkRoto}')

    except Exception as exc:
        print(f'Vaya, ha habido un error: {exc}')

# Establece la web y ejecuta el programa.       
web = 'https://automatetheboringstuff.com/'
if __name__ == "__main__":
    verificador(web)
    pass