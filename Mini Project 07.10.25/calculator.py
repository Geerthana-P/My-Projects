num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")
if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    print("Result:", num1 / num2)  
else :
    print("Invalid operator! Please enter +, -, * or /.")  