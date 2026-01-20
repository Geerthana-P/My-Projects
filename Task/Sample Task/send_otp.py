import smtplib
import random

# Generate OTP
otp = random.randint(100000, 999999)

# Email credentials
sender = ""      # your email
password = ""    # your app password (NOT Gmail login password)
receiver = ""    # receiver email

# Email message
message = f"Subject: Your OTP\n\nYour OTP is {otp}"

# Sending email
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()

print("OTP sent to email!")
