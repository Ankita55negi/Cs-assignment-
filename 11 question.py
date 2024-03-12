# Function to generate Fibonacci sequence up to n terms using while loop
def generate_fibonacci(n):
    fibonacci_seq = []
    a, b = 0, 1
    count = 0
    while count < n:
        fibonacci_seq.append(a)
        a, b = b, a + b
        count += 1
    return fibonacci_seq

# Input: number of terms
n = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generate Fibonacci sequence up to n terms
fibonacci_sequence = generate_fibonacci(n)

# Display the Fibonacci sequence
print("Fibonacci sequence up to", n, "terms:")
print(fibonacci_sequence)