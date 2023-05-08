import os
import subprocess
import smtplib
from email.mime.text import MIMEText

# Directorio raiz del repositorio de GitHub
repo_dir = "/path/to/repo"

# Comando para ejecutar las pruebas
test_command = "python -m unittest discover tests"

# Direccion de correo electronico y contrasena del remitente
from_email = "correo@empresa.com"
password = "contrasena"

# Direcciones de correo electronico de los destinatarios
to_emails = ["miembro1@empresa.com", "miembro2@empresa.com"]

# Ejecutar las pruebas
result = subprocess.run(test_command, shell=True, cwd=repo_dir)

# Enviar notificacion por correo electronico segun el resultado de las pruebas
if result.returncode == 0:
    subject = "Las pruebas han pasado"
    body = "Todas las pruebas han pasado satisfactoriamente."
else:
    subject = "Las pruebas han fallado"
    body = "Al menos una prueba ha fallado. Por favor, revise el codigo."
    
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = ", ".join(to_emails)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_email, password)
server.sendmail(from_email, to_emails, msg.as_string())
server.quit()