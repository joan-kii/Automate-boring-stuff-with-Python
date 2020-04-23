#!python3
# randomChoreAssignmentEmailer.py Envía emails con la asignación de las tareas
# semanales con Gmail. 

import ezgmail, random, os

# Lista de tareas.
tareas = ['pasear al perro', 'limpiar la arena de los gatos', 'hacer la compra', 'lavar el coche']

# Lista de emails.
emailsDict = {'Messi':'messi@ejemplo.com', 'Pelé':'pele@ejemplo.com', 'Maradona':'maradona@ejemplo.com', 'Arbeloa':'arbeloa@ejemplo.com'}

# Inicia el módulo 'ezgmail'
ezgmail.init()

# Itera por la lista de emails, elige una tarea de la lista de forma
# aleatoria y envía el email.
for nombre in emailsDict:
    tareaRandom = random.choice(tareas)
    # Establece asunto y mensaje.
    asunto = 'La tarea semanal.'
    mensaje = f'Y la tarea que te ha tocado esta semana es... {tareaRandom}.\nÁnimo {nombre}!!'
    ezgmail.send(emailsDict[nombre], asunto, mensaje)
    # Elimina la tarea asignada para evitar asignarla otra vez.
    tareas.remove(tareaRandom)