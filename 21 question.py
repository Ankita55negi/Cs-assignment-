# Function to check if element is present in array
def is_element_present(arr, element):
    for item in arr:
        if item == element:
            return True
    return False

# Input: an array of elements and the element to check
arr = [1, 2, 3, 4, 5]
element = int(input("Enter the element to check: "))

# Check if element is present in the array
if is_element_present(arr, element):
    print("Element", element, "is present in the array.")
else:
    print("Element", element, "is not present in the array.")