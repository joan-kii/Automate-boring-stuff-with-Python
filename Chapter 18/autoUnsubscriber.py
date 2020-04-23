#!python3
# autoUnsubscriber.py Abre el email, enlaza a todos los links
# de 'unsubscribe' y carga las páginas.

import imapclient, pyzmail, webbrowser, bs4, sys

# Establece el email, y obtiene la contraseña de la línea de comandos.
email = 'giggs@ejemplo.com'
contraseña = sys.argv[1]
# Conecta con el servidor Outlook.
imapObj = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True)
imapObj.login(email, contraseña)

# Selecciona la Bandeja de Entrada y busca la palabra clave
# 'unsubscribe'.
imapObj.select_folder('INBOX', readonly=True)
emailsID = imapObj.search(['ALL'])
mensajes = imapObj.fetch(emailsID, [b'BODY[]'])
palabraClave = 'Unsubscribe'

# Itera sobre la lista de emails y abre los links en el navegador.
for mail in emailsID:
    try:
        # Obtiene el texto del email.
        texto = pyzmail.PyzMessage.factory(mensajes[mail][b'BODY[]'])
        htmlObj = texto.html_part.get_payload().decode(texto.html_part.charset)
        # Busca elemetos etiquetados como 'a'. (links)
        soup = bs4.BeautifulSoup(htmlObj, 'html.parser')
        links = soup.select('a')

        # Itera por la lista de links y si aparece la palabra clave
        # abre la página.
        for link in links:
            if palabraClave in link.text:
                url = link.get('href')
                webbrowser.open(url)
    # Informa al usuario en caso de un error en la carga.
    except Exception:
        print('Ha habido un error al abrir este enlace.')
        continue