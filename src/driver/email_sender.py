from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(to_address, body):
    from_address = "b34xb3gjlwcx3gxb@ethereal.email"
    login = "b34xb3gjlwcx3gxb@ethereal.email"
    password = "pmpNxyFupVGhx3DAHr"
    msg = MIMEMultipart()
    msg["from"] = "confirm@trip-planner.com"
    msg["to"] = to_address
    msg["subject"] = "Confirm your participation"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()
