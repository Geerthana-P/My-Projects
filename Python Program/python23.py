# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculating difference
if num1 > num2:
    difference = num1 - num2
    print("First number is greater")
elif num2 > num1:
    difference = num2 - num1
    print("Second number is greater")
else:
    difference = 0
    print("Both numbers are equal")

print("Difference:", difference)
