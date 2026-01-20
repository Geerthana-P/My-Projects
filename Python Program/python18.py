# Taking input from user
num = int(input("Enter a number: "))

# Considering positive numbers only for digit count
num_abs = abs(num)

if num_abs < 10:
    print("Single-digit number")
elif num_abs < 100:
    print("Double-digit number")
else:
    print("Multi-digit number")
