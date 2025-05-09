# What is a dictionary?
# A dictionary in Python is a collection of key-value pairs. 
# Each key is unique, and it is used to store and retrieve values efficiently.
# Dictionaries are mutable, meaning you can change their content after creation.

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print(my_dict["name"])  # Output: Alice

# Adding a new key-value pair
my_dict["job"] = "Engineer"
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}

# Updating a value
my_dict["age"] = 26
print(my_dict) # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}

# Removing a key-value pair
del my_dict["city"]
print(my_dict) 

# Using the get() method
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("city", "Not Found"))  # Output: Not Found

# Iterating through keys
for key in my_dict:
    print(key, my_dict[key])

# Iterating through values
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value)  # Output: name Alice, age 26, job Engineer

# Checking if a key exists
if "name" in my_dict:
    print("Key 'name' exists")

# Dictionary comprehension
squared_numbers = {x: x**2 for x in range(5)}
print(squared_numbers) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Nested dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(nested_dict["person1"]["name"])  # Output: Alice

# Clearing a dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# Copying a dictionary
original = {"a": 1, "b": 2}
copy = original.copy()
print(copy) # Output: {'a': 1, 'b': 2}

# Merging dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

# pop() method removes the last inserted key-value pair
dict1.pop("a")
print(dict1)  # Output: {'b': 2}