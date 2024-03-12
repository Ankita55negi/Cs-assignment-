# Function to remove k-th character from a string
def remove_kth_character(s, k):
    # Check if k is a valid index
    if k < 0 or k >= len(s):
        return "Invalid index"
    # Remove the k-th character and return the updated string
    return s[:k] + s[k+1:]

# Input: a string and the index of the character to remove
s = input("Enter a string: ")
k = int(input("Enter the index of the character to remove: "))

# Remove the k-th character from the string
result = remove_kth_character(s, k)

# Display the result
print("String after removing k-th character:", result)