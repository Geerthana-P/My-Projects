# Predefined username and password
correct_username = "admin"
correct_password = "12345"

# Taking input from user
username = input("Enter username: ")
password = input("Enter password: ")

# Validating login
if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")
