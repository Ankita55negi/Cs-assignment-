# Function to find nth-largest and nth-smallest elements in a list
def find_nth_elements(numbers, n):
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    # Find the nth-smallest element
    nth_smallest = sorted_numbers[n - 1]
    # Find the nth-largest element
    nth_largest = sorted_numbers[-n]
    return nth_smallest, nth_largest

# Input: a list of numbers and the value of n
numbers = [int(x) for x in input("Enter the list of numbers separated by space: ").split()]
n = int(input("Enter the value of n: "))

# Find the nth-largest and nth-smallest elements
nth_smallest, nth_largest = find_nth_elements(numbers, n)

# Display the results
print("The", n, "th-smallest element is:", nth_smallest)
print("The", n, "th-largest element is:", nth_largest)