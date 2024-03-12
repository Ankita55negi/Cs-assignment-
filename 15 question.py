# Function to check if a number is binary
def is_binary(number):
    # Iterate over each digit of the number
    for digit in str(number):
        # If the digit is not 0 or 1, return False
        if digit != '0' and digit != '1':
            return False
    # If all digits are 0 or 1, return True
    return True

# Input: a number
number = input("Enter a number: ")

# Check if the number is binary
if is_binary(number):
    print(number, "is a binary number.")
else:
    print(number, "is not a binary number.")