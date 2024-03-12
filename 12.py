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

# Input: an integer n
n = int(input("Enter the value of n: "))

# Find all prime numbers from 1 to n
prime_numbers = [num for num in range(1, n+1) if is_prime(num)]

# Display the result
print("Prime numbers from 1 to", n, "are:")
print(prime_numbers)