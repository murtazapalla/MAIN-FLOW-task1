# Create an empty set
my_set = set()

# Add elements to the set
my_set.add(1)
my_set.add(2)
my_set.add(3)
print("Set after adding elements:", my_set)

# Remove an element from the set
my_set.remove(2)
print("Set after removing an element:", my_set)

# # Discard an element from the set (no error if element doesn't exist)
# my_set.discard(4)
# print("Set after discarding an element:", my_set)

# Modify an element in the set
if 1 in my_set:
    my_set.remove(1)
    my_set.add(5)
print("Set after modifying an element:", my_set)

# # Get the number of elements in the set
# print("Number of elements in the set:", len(my_set))

# # Create a set with initial elements
# another_set = {4, 5, 6}
# print("Another set with initial elements:", another_set)


