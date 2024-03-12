# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Input: a number
num = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")