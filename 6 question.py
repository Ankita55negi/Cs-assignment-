# Function to find maximum and minimum of n numbers
def find_max_min(numbers):
    if not numbers:
        return None, None
    
    max_num = numbers[0]
    min_num = numbers[0]
    
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
            
    return max_num, min_num

# Input: n numbers
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = float(input("Enter number {}: ".format(i+1)))
    numbers.append(num)

# Find maximum and minimum of n numbers
max_num, min_num = find_max_min(numbers)

# Display the result
print("Maximum number:", max_num)
print("Minimum number:", min_num)