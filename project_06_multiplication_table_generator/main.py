# Multiplication Table Generator

# Get a number from the user
number = int(input("Enter a number: "))

# Print the multiplication table using a for loop
print(f"\nMultiplication Table of {number}\n" + "-" * 30)

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")