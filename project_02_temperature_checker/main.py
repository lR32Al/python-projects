# Ask the user to enter the temperature of their city
temperature = int(input("Tell me your city's temperature: "))

# Check and print a message based on the temperature range
if temperature >= 30:
    print("Wow, that's totally hot!")
elif 20 < temperature < 30:
    print("Definitely it's nice weather.")
elif 0 <= temperature <= 20:
    print("Yup, it's cold weather.")
else:
    print("Freezing!")
