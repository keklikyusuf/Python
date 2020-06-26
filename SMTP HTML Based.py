# Import related tools

import smtplib as smtp
from email.mime.multipart import MIMEMultipart    # This is imported to be able to handle HTML tags
from email.mime.text import MIMEText                    # This is imported to be able to handle HTML tags

server = 'smtp.gmail.com'
port = 587

# Establishment connection to SMTP
connection = smtp.SMTP(server, port)
connection.ehlo()
connection.starttls()
print('Connection has been  Established Successfully!')

email = 'abc@gmail.com'
password = 'acb.'

connection.login(email, password)

# Create an OBJECT to store related values
tmessage = MIMEMultipart('alternative')  # Indentifies HTML tags

tmessage['Subject'] = 'HTML Message'
tmessage['From'] = email
tmessage['To'] = email

# From to To description
_FROM = email
_TO = email

# Create HTML based message
html_message = '''' <html>
                        <body>
                            <h1> House Prices </h1>
                            <p> This is main list of the House Prices
                        </body>
                    </html>'''

# Create an OBJECT to RENDER HTML
msg = MIMEText(html_message, 'html')    # Renders HTML Messages

# Attaches created message to the tmessage object
tmessage.attach(msg)

connection.sendmail(_FROM, _TO, tmessage.as_string())
print('EMAIL HAS BEEN SENT!')

connection.quit()