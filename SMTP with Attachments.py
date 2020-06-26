# Import all related methods
import smtplib as smtp
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Decided SERVER and PORT numbers
server = 'smtp.gmail.com'
port = 587

# Related data will be go into the created Object for Message
email_from = 'abc@gmail.com'
email_to = 'def@gmail.com'
email_password = 'abcdef'
email_subject = 'Bla Bla Reports'

# Created Message as Object and inserted variables
message = MIMEMultipart()   # Created instance as Multipart
message['Subject'] = 'Bla Bla Reports'  # Variables for created Instance
message['From'] = email_from    # Variables for created Instance
message['To'] = email_to    # Variables for created Instance

# This file will be included at attachment
fileName = 'blabla.txt'
openFile = open(fileName, 'rb')

# This Object has been used to attach the file above
mimref = MIMEBase('application', 'octect-stream')
mimref.set_payload((openFile.read()))
encoders.encode_base64(mimref)
mimref.add_header('Content-dispostion', 'openfile;filename='+fileName)
message.attach(mimref)

# Connection to SMTP
connection = smtp.SMTP(server, port)
connection.starttls()

# Connection to Email Address
connection.login(email_from, email_password)
connection.sendmail(email_from, email_to, message.as_string())

# Close Email Connection After Sending the Email
connection.quit()