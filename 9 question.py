# Function to count the occurrence of each element in the list
def count_occurrences(numbers):
    occurrences = {}
    for num in numbers:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1
    return occurrences

# Input: list of numbers
numbers = [int(x) for x in input("Enter the list of numbers separated by space: ").split()]

# Count the occurrence of each element in the list
occurrences = count_occurrences(numbers)

# Display the result
print("Occurrence of each element in the list:")
for key, value in occurrences.items():
    print(key, ":", value)