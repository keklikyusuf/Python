import smtplib as smtp

# This is used SMTP Server which is Gmail for this application
server = 'smtp.gmail.com'
port = 587
# Server name and port number is specified for Gmail in this case,
# If you want to use other mail services you can find their SMTP server name and port numbers
# Go to:
# if it is POP3 : https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html
# if it is IMAP : https://www.arclab.com/en/kb/email/list-of-smtp-and-imap-servers-mailserver-list.html

# Now, e-mail and its password will be assigned for usage
email = 'abcd@gmail.com'
password = 'abcabc.'

# Getting Connection to the SMTP server of the E-Mail Service with including two main arguments 'server' and 'port'
try:
    connection = smtp.SMTP(server, port)
    connection.ehlo()       # This line establishes secure connection with SMTP
    connection.starttls()   # This line establishes secure connection with SMTP
    print('Connection with Server and Port# is successful!')
    # Getting logged In to dedicated e mail address with two main arguments 'email' and 'password'
    try:
        connection.login(email, password)
        print('Log in attempt successful!')
    except:
        print('Log in attempt failed!')
except:
    print('Connection Failed')

_From = 'abc@gmail.com'
_To = [_From, 'abcc@gmail.com', 'deff@gmail.com', 'klmm@gmail.com']
message = "This is the e mail send using the SMTP Gmail Server!"

connection.sendmail(_From, _To, message)
print('Message has  been sent!')

connection.quit()
