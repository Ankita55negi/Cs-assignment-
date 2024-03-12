# Function to find factorial of given number

def factorial(n):

       

    res = 1

      

    for i in range(2, n+1):

        res *= i

    return res

 # Driver Code

num = 5

print("Factorial of", num, "is",
factorial(num))