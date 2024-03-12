# Function to find the first occurrence of number divisible by K in the list
def first_occurrence_divisible_by_k(numbers, k):
    for num in numbers:
        if num % k == 0:
            return num
    return None

# Input: list of numbers and K
numbers = [int(x) for x in input("Enter the list of numbers separated by space: ").split()]
k = int(input("Enter the value of K: "))

# Find the first occurrence of number divisible by K
result = first_occurrence_divisible_by_k(numbers, k)

# Display the result
if result:
    print("First occurrence of number divisible by", k, "is:", result)
else:
    print("No number in the list is divisible by", k)