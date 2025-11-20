import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Allow the user 3 attempts
attempts = 3

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        print("You win! 🎉")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Try again! You have", attempts, "attempt(s) left.")
        else:
            print("Game over! 😢 The number was", secret_number)
