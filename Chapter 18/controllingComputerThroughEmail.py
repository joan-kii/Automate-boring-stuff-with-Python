#!python3
# controllingComputerThroughEmail.py Realiza las descargas solicitadas
# por email. 

import logging, subprocess, time, imapclient, pyzmail

# Confugura sistema de depuración.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.disable(logging.INFO)

def emuleDownload():
    """ Esta función conecta con el servidor de correo electrónico y
        comprueba si hay alguna petición de descarga de archivos.
        
        Si hay alguna petición, comprueba que provenga de un email
        autorizado, que tenga el password de acceso, realiza la 
        descarga a través de emule y elimina los emails. """

    # Conexión con el servidor de correo electrónico.
    try:
        logging.debug('Comprobando email.')
        imapObj = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True)
        imapObj.login(email, passwordEmail)
    except Exception:
        logging.debug('Conexión servidor Outlook.')
        print('\nHa habido un error en la conexión con el servidor de Outlook.\n')
        time.sleep(5)
        return None

    #Comprueba si en la bandeja de netrada hay algún email con el asunto
    # 'descarga'. 
    imapObj.select_folder('INBOX', readonly=True)
    listaEmails = imapObj.search('SUBJECT Descarga')
    if listaEmails != []:
        logging.debug(f'Lista de emails: ({listaEmails})')
    else: 
        print('\nNo hay ninguna descarga pendiente.\n')
        time.sleep(5)
        return None

    # Comprueba que el mensaje provenga de una dirección de correo
    # electrónico autorizado.
    links = []
    for item in listaEmails:
        textoMensaje = imapObj.fetch([item], ['BODY[]'])
        mensaje = pyzmail.PyzMessage.factory(textoMensaje[item][b'BODY[]'])
        # Obtiene la dirección de correo remitente.
        remitente = mensaje.get_address('from')

        # Si el remitente está en la lista de autorizados
        #  continúa con el proceso.
        if remitente[1] in emailsAutorizados:
            texto = mensaje.text_part.get_payload().decode(mensaje.text_part.charset)
            logging.info(f'Email autorizado: ({remitente[1]})')
            logging.debug('Texto email.')
        else: 
            logging.info(f'Email no autorizado: ({remitente[1]})')
            print('\nExiste una petición de descarga pero no procede de un Email Autorizado.\n')
            continue

        # Si la contraseña aparece en el texto, obtiene el link de 
        # descarga y lo añade a la lista de links.
        if passwordDescarga in texto:
            link = mensaje.html_part.get_payload().decode(mensaje.html_part.charset)
            logging.debug('Link descarga.')
            links.append(link)
        else: 
            logging.info(f'Contraseña inválida: (({remitente[1]})')
            print('\nExiste una petición de descarga de un Email Autorizado pero la contraseña no es correcta.\n')

    # Elimina los emails con peticiones de descarga.
    try:
        print('\nEliminando los emails con solicitudes de descarga...\n')
        imapObj.delete_messages(listaEmails)
        imapObj.expunge()
        logging.debug(f'Eliminando emails ({listaEmails})')
    except Exception:
        logging.debug('No se han podido eliminar todos los email con solicitudes de descarga.')

    # Cierra la sesión en el servidor de email.
    imapObj.logout()
    # Devuelve la lista de enlaces de descarga.
    return links

# Establece ruta de ejecución del programa de descargas, email, password
# de acceso a email, password de descarga y lista de emails autorizados.
emule = r'C:\tu_path\eMule\emule.exe'    
email = 'ronaldinho@ejemplo.com'
passwordEmail = 'joga_bonito'
passwordDescarga = 'descarga_esta!'
emailsAutorizados = ['batistuta@ejemplo.com', 'puskas@ejemplo.com']

# Llama a la función cada 15 minutos y si hay alguna petición, ejecuta 
# emule e itera por la lista de links iniciando la descarga de cada link.
while True:
    descargas = emuleDownload()
    if descargas != None:
        logging.info(f'Número de descargas solicitadas: ({len(descargas)})')
        for descarga in descargas:
            subprocess.Popen(emule)
            time.sleep(15)
            subprocess.Popen(emule + ' ' + descarga)

    time.sleep(900)


