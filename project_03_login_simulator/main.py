# Login Simulator

# Initialize attempt counter
attempts = 0

# Allow up to 3 login attempts
while attempts < 3:
    name = input("Please tell us your name: ")
    password = int(input("Please tell us your password: "))

    # Check if both username and password are correct
    if name == "reza" and password == 1234:
        print("Welcome!")
        break
    else:
        print("Try again.")
        attempts += 1

# If the user fails 3 times, deny access
if attempts == 3:
    print("Too many tries. Access denied.")
