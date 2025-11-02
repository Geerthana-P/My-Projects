# Simple Calculator Program

while True:
    print("\nSimple Calculator")
    print("Choose an operation (+, -, *, /) or type 'exit' to quit")

    operation = input("Enter operation: ")

    if operation == "exit":
        print("Exiting calculator")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero!")
            continue
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
        continue

    print(f"The result is: {result}")
