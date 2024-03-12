# Input: list of names
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heather", "Ivan"]

# Print names whose length is greater than 6
print("Names with length greater than 6:")
for name in names:
    if len(name) > 6:
        print(name)