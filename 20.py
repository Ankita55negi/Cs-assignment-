# Function to check if a list is monotonic
def is_monotonic(lst):
    increasing = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    decreasing = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
    return increasing or decreasing

# Input: a list of numbers
numbers = [int(x) for x in input("Enter the list of numbers separated by space: ").split()]

# Check if the list is monotonic
if is_monotonic(numbers):
    print("The list is monotonic.")
else:
    print("The list is not monotonic.")