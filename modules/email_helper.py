import smtplib
import email
import ssl
import os
import modules.config as config


def prepare_email(sender, recipient, message):
    email_message = email.message.Message()
    email_message.add_header('from', f"{config.APP_TITLE} <{sender}>")
    email_message.add_header('to', recipient)
    email_message.add_header('subject', f"[{config.APP_TITLE}] New Message Received")
    email_message.set_payload(f"Sender:\n{sender}\n\nMessage:\n{message}")

    return email_message.as_string()


def send_email(sender, message):
    host = config.APP_EMAIL_HOST
    port = config.APP_EMAIL_PORT
    username = os.getenv("APP_EMAIL_USER")
    password = os.getenv("APP_EMAIL_PASS")
    context = ssl.create_default_context()
    recipient = os.getenv("APP_EMAIL_INBOX")

    email_message = prepare_email(sender, recipient, message)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(sender, recipient, email_message)
