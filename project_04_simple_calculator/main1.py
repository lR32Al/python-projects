# Simple Calculator

# Ask the user for two numbers
num1 = float(input("Give number 1: "))
num2 = float(input("Give number 2: "))

# Ask the user to choose an operator
operator = input("Select your operator (+, -, *, /): ")

# Perform calculation based on the operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"
else:
    result = "You chose a wrong character."

# Display the result
print("Result:", result)
