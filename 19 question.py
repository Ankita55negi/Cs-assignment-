# Input: a string
string = input("Enter a string: ")

# Print ASCII value of each character
print("ASCII values of characters in the string:")
for char in string:
    ascii_value = ord(char)
    print(char, ":", ascii_value)