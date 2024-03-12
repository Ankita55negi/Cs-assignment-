# Function to check if a string is palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Compare the string with its reverse
    return s == s[::-1]

# Input: a string
s = input("Enter a string: ")

# Check if the string is palindrome
if is_palindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")