import imaplib 
import os
import email 
from email.header import decode_header


# Using environment variables for credentials
email_address = os.environ.get("EMAIL_ADDRESS", "your-email@appogee.com")
password = os.environ.get("EMAIL_PASSWORD", "yourpassword")
server = "outlook.office365.com"

def connect_to_email(server, email, password):
    try:
        mail = imaplib.IMAP4_SSL(server)
        mail.login(email, password)
        print("Successfully connected to the email server.")
        return mail
    except Exception as e:
        print(f"Failed to connect to the email server: {e}")
        return None

# Function to fetch emails
def fetch_emails(mail, folder='INBOX', search_criteria='ALL'):
    try:
        mail.select(folder)
        status, messages = mail.search(None, search_criteria)
        if status == 'OK':
            # Returning message IDs
            return messages[0].split()
        else:
            print("Failed to fetch emails.")
            return []
    except Exception as e:
        print(f"Error fetching emails: {e}")
        return []

# Example usage
if __name__ == "__main__":
    mail = connect_to_email(server, email_address, password)
    if mail is not None:
        messages = fetch_emails(mail)
        print(f"Number of emails fetched: {len(messages)}")