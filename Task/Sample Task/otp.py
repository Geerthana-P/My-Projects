import random
import time

def generate_otp():
    otp = random.randint(100000, 999999)
    expiry_time = time.time() + 10   # OTP valid for 10 seconds
    return otp, expiry_time

def verify_otp(user_input, otp, expiry_time):
    if time.time() > expiry_time:
        return "OTP expired!"
    elif user_input == otp:
        return "OTP verified successfully!"
    else:
        return "Invalid OTP!"

# Generate OTP
otp, expiry = generate_otp()
print("Your OTP is:", otp)

# Wait for user to enter the OTP
time.sleep(5)     # simulate delay (optional)

user_otp = int(input("Enter OTP: "))
result = verify_otp(user_otp, otp, expiry)
print(result)
