# Ask the user to describe their personality
sentence = input("Tell me about your personality please: ")

# Length of the sentence
print("Length of your sentence:", len(sentence))

# Check if the word "reza" is mentioned in the sentence
if "reza" in sentence.lower():
    print("Your sentence mentions 'reza'!")
else:
    print("'reza' is not mentioned.")

# Display the first and last characters of the sentence
print("First character:", sentence[0])
print("Last character:", sentence[-1])

# Count spaces (useful for estimating the number of words)
spaces = sentence.count(" ")
print("Number of spaces:", spaces)

# Display the first 5 characters of the sentence
print("First 5 characters:", sentence[:5])
