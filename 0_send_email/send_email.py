import smtplib, ssl
from email.message import EmailMessage

subject = 'Sending dummy message'
sender = "dridi.chaith@gmail.com"
receiver = " dridi.chaith.30@gmail.com"
msg_content = """
Trying to send a message to test sending messages
using python
"""
password = "xxcp vrjh gsgo mcsc"
port = 465
smtp_server = "smtp.gmail.com"

msg = EmailMessage()
msg.set_content(msg_content)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.send_message(msg, from_addr=sender, to_addrs=receiver)
