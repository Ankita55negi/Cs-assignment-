# Function to check if a number is an Armstrong number
def is_armstrong(number):
    # Convert the number to a string to get its length
    num_str = str(number)
    # Calculate the power to which each digit should be raised
    power = len(num_str)
    # Calculate the sum of the digits raised to the power
    total = sum(int(digit) ** power for digit in num_str)
    # Check if the sum is equal to the original number
    return total == number

# Input: a number
number = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")