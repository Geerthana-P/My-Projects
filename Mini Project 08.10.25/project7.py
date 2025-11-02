import random

def generate_password(length, use_numbers=True, use_symbols=True):

    lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
    uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    char_pool = lowercase_chars + uppercase_chars

    if use_numbers:
        char_pool += numbers
    if use_symbols:
        char_pool += symbols

    password = ""
    for _ in range(length):
        password += random.choice(char_pool)

    return password

print("Simple password (only letters):", generate_password(8, False, False))
print("Password with numbers:", generate_password(10, True, False))
print("Strong password (with numbers & symbols):", generate_password(12, True, True))
