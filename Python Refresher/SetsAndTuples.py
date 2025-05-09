# 2. Tuples
# Definition: An ordered, immutable (unchangeable) collection of items.
# Key Features:
# Items are stored in the order they are added.
# Cannot modify, add, or remove items after creation.
# Allows duplicate items.
# Use Case: When you need a fixed, ordered collection of items that should not change.

# A tuple of coordinates
coordinates = (10, 20, 30)
print(coordinates)  # Output: (10, 20, 30)

# Tuples are immutable
# coordinates[0] = 15  # This will raise an error

# Example: Tuples
# Accessing elements in a tuple
coordinates = (10, 20, 30)
print(coordinates[0])  # Output: 10

# Tuple unpacking destructuring
x, y, z = coordinates
print(x, y, z)  # Output: 10 20 30

# 3. Sets
# Definition: An unordered, mutable collection of unique items.
# Key Features:
# Items are not stored in any specific order.
# Does not allow duplicate items.
# Supports set operations like union, intersection, and difference.
# Use Case: When you need a collection of unique items or want to perform mathematical set operations.

# Example: Sets
# Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'} (order may vary)

# Adding an item to a set
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'} (order may vary)

# Removing an item from a set
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'} (order may vary)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
list_city_name = ["London", "Paris", "New York"]
list_city_sub_name = ["London", "California", "Los Angeles"]
print(set_a.union(set_b))        # Output: {1, 2, 3, 4, 5}
print(set_a.intersection(set_b)) # Output: {3}
print(list_city_name.intersection(list_city_sub_name))   # Output: ['London']
print(list_city_sub_name.difference(list_city_name))    # Output: ['California', 'Los Angeles']

print(list_city_sub_name.intersection(list_city_name)) # Output: ['London']

print(set_a.intersection(set_b))  
# print(set_a[0])  # This will raise an error because sets are unordered
