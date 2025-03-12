print("Welcome to the simple calculator!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("What operation do you want to perform (+, -, *, /): ")

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
        result = "Sorry, you can't divide by zero!"
else:
    result = "Invalid operation! Please choose one of these: +, -, *, /"

# Show the result
print(f"Result: {num1} {operation} {num2} = {result}")
