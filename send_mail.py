import smtplib, ssl
import os
from email.mime.text import MIMEText

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    username = "brainframeapps@gmail.com"
    password = os.environ.get("APPPASSWORD")

    if not password:
        raise ValueError("App password not found in environment variable 'APPPASSWORD'. Please set it.")

    receiver = "brainframeapps@gmail.com"
    # Create a MIMEText object with UTF-8 encoding
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = username
    msg['To'] = receiver
    msg['Subject'] = "Test Email from Python"

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, msg.as_string())
            print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication failed: {e}. Check your app password and Gmail security settings.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    message = "This is a test message from send_mail applet"  # Can include smart quotes like ’
    send_mail(message)