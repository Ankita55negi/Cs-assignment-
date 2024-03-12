# Function to find the sum of digits of a number
def sum_of_digits(number):
    # Convert the number to a string to iterate over its digits
    number_str = str(number)
    # Initialize sum to 0
    total = 0
    # Iterate over each digit and add it to the sum
    for digit in number_str:
        total += int(digit)
    return total

# Input: a number
number = int(input("Enter a number: "))

# Find the sum of digits of the number
sum_digits = sum_of_digits(number)

# Display the result
print("Sum of digits of", number, "is:", sum_digits)