# Function to remove vowels from a string
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    # Use list comprehension to create a new string without vowels
    return ''.join([char for char in s if char not in vowels])

# Input: a string
s = input("Enter a string: ")

# Remove vowels from the string
result = remove_vowels(s)

# Display the result
print("String after removing vowels:", result)