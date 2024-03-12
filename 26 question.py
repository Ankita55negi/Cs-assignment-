# Input: a string
string = input("Enter a string: ")

# Print characters whose length is even
print("Characters whose length is even:")
for char in string:
    if len(char) % 2 == 0:
        print(char)