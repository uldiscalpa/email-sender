from email import message
import smtplib
import ssl
from message_creator import Message
from config import EMAIL_FROM, PASSWORD

# Create a secure SSL context


class EmailSender:
    
    def __init__(self):
        pass
        

def send(message):
    """send email"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EMAIL_FROM, PASSWORD)
        for m in message:
            server.send_message(m)
        
if __name__ == '__main__':
    mail_from = 'uldis.calpa@gmail.com'
    mail_to = 'uldis.calpa@kurbads.lv'
    subject1 = 'Virsraksts1'
    subject2 = "Ziemassvētku virsraksts"
    plain_text_1 = "Sveiciens \n svētkos \n un vēl viss kas cits"
    plain_text_2 = "Čau"

    message1 = Message(mail_from, mail_to, subject1, plain_text_1)
    message2 = Message(mail_from, mail_to, subject2, plain_text_2)
    
    send([message1.message, message2.message])