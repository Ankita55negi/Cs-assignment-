# Function to check if substring is present in string
def is_substring_present(s, substring):
    if substring in s:
        return True
    else:
        return False

# Input: a string and a substring
s = input("Enter a string: ")
substring = input("Enter a substring to check: ")

# Check if substring is present in the string
if is_substring_present(s, substring):
    print("Substring", substring, "is present in the string.")
else:
    print("Substring", substring, "is not present in the string.")