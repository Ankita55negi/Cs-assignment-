# Function to find the nth Fibonacci number
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Input: a positive integer
n = int(input("Enter a positive integer n: "))

# Display the nth Fibonacci number
result = fibonacci(n)
print("The", n, "th Fibonacci number is:", result)