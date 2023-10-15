import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Generate a random 6-digit OTP
def generate_otp():
    return ''.join(random.choice(string.digits) for _ in range(6))


# Email configuration
sender_email = "akiwelekar@gmail.com"
sender_password = "pxue ssll qagm chhu"
recipient_email = "awk@dbatu.ac.in"

# Generate OTP
otp = generate_otp()

# Create the email content
subject = "Your OTP Code"
message = f"Your OTP code is: {otp}"

# Setup the email server
smtp_server = "smtp.gmail.com"
smtp_port = 587

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Create and send the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

    print(f"OTP sent to {recipient_email}")

except smtplib.SMTPException as e:
    print(f"An error occurred: {e}")
