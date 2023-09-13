from email.message import EmailMessage
import ssl
import smtplib

email_send = 'legitness2003@gmail.com'
email_pw = 'qudnwxxiiofhxsrg'
email_receive = 'stewartt3@wit.edu'

subject = 'Weather for the Week'
body = """
Yo what's up. 
""" 

em = EmailMessage()
em['From'] = email_send
em['To'] = email_receive
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_pw)
    s mtp.sendmail(email_send, email_receive, em.as_string())