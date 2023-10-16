import smtplib
import random
import re
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "akiwelekar@gmail.com"
sender_password = "pxue ssll qagm chhu"
recipient_email = "awk@dbatu.ac.in"
LENGTH = 6

# Generate a random 6-digit OTP
def generate_otp(LENGTH):
return ''.join(random.choice(string.digits) for _ in range(LENGTH))

def send_otp_mail(sender, sender_password, receiver, otp):
# Create the email content
subject = "Your OTP Code"
message = f"Your OTP code is: {otp}"

# Setup the email server
smtp_server = "smtp.gmail.com"
smtp_port = 587

try:
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender, sender_password)

# Create and send the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

server.sendmail(sender, receiver, msg.as_string())
server.quit()

print(f"OTP sent to {receiver}")

except smtplib.SMTPException as e:
print(f"An error occurred: {e}")

def validate_email(email):
# Regular expression for basic email validation
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# Use the re.match function to check if the email matches the pattern
if re.match(pattern, email):
return True
else:
return False

# Generate OTP
otp = generate_otp(LENGTH)

if (not validate_email(recipient_email)):
print ("Wrong Email ID")

if (validate_email(recipient_email)):
send_otp_mail(sender_email,sender_password, recipient_email, otp)

