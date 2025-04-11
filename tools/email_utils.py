import imaplib
import smtplib
import email
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import time

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

def fetch_unread_emails():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")
        _, data = mail.search(None, 'UNSEEN')
        email_ids = data[0].split()

        emails = []
        for e_id in email_ids:
            _, msg_data = mail.fetch(e_id, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    emails.append({
                        "subject": msg["subject"],
                        "from": msg["from"],
                        "body": get_body(msg)
                    })
        mail.logout()
        return emails
    except Exception as e:
        print(f"An error occurred while fetching emails: {e}")
        return []

def get_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_dispo = str(part.get('Content-Disposition'))

            if content_type == 'text/plain' and 'attachment' not in content_dispo:
                charset = part.get_content_charset() or 'utf-8'
                try:
                    return part.get_payload(decode=True).decode(charset, errors='replace')
                except Exception as e:
                    print(f"Decode error: {e}")
                    return part.get_payload(decode=True).decode('utf-8', errors='replace')
    else:
        charset = msg.get_content_charset() or 'utf-8'
        try:
            return msg.get_payload(decode=True).decode(charset, errors='replace')
        except Exception as e:
            print(f"Decode error: {e}")
            return msg.get_payload(decode=True).decode('utf-8', errors='replace')

def send_email(sender_email, receiver_email, subject, body, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, sender_password=PASSWORD):
    try:
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

       
        retries = 3 
        for _ in range(retries):
            try:
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()  
                    server.login(sender_email, sender_password)  
                    server.sendmail(sender_email, receiver_email, msg.as_string())  
                    print("Email sent successfully!")
                    break
            except smtplib.SMTPServerDisconnected:
                print("The connection to the SMTP server was unexpectedly closed. Retrying...")
                time.sleep(5) 
            except Exception as e:
                print(f"An error occurred while sending the email: {e}")
                break
    except Exception as e:
        print(f"An error occurred: {e}")

