# Simple Calculator using Function

def calculator(num1, num2, operator):
    """Simple calculator function"""
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "You chose a wrong character."


# --- Using the function ---
n1 = float(input("Give number 1: "))
n2 = float(input("Give number 2: "))
op = input("Select your operator (+, -, *, /): ")

result = calculator(n1, n2, op)
print("Result:", result)
