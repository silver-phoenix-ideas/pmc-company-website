import smtplib
import email
import ssl
import os
import modules.config as config


def get_email_subject(topic):
    subject = f"[{config.APP_TITLE}] "

    match topic:
        case "Job Inquiries":
            subject += "New Job Inquiry Received"
        case "Project Proposals":
            subject += "New Project Proposal Received"
        case _:
            subject += "New Message Received"

    return subject


def prepare_email(sender, recipient, topic, message):
    email_message = email.message.Message()
    email_message.add_header('from', f"{config.APP_TITLE} <{sender}>")
    email_message.add_header('to', recipient)
    email_message.add_header('subject', get_email_subject(topic))
    email_message.set_payload(
        f"Sender:\n{sender}\n\nTopic:\n{topic}\n\nMessage:\n{message}"
    )

    return email_message.as_string()


def send_email(sender, topic, message):
    host = config.APP_EMAIL_HOST
    port = config.APP_EMAIL_PORT
    username = os.getenv("APP_EMAIL_USER")
    password = os.getenv("APP_EMAIL_PASS")
    context = ssl.create_default_context()
    recipient = os.getenv("APP_EMAIL_INBOX")

    email_message = prepare_email(sender, recipient, topic, message)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(sender, recipient, email_message)
