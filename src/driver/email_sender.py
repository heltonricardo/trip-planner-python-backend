from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


# Execute the code from `~\utils\create_email.py` to get credentials to test.
# Log in to your account in https://ethereal.email/login to see the emails.

USER = "b34xb3gjlwcx3gxb@ethereal.email"
PASS = "pmpNxyFupVGhx3DAHr"


def send_email(to_address: str, body: str):
    login = USER
    password = PASS
    from_address = USER
    msg = MIMEMultipart()
    msg["from"] = "confirm@trip-planner.com"
    msg["to"] = to_address
    msg["subject"] = "Confirm Your Trip!"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()
