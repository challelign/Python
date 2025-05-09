"""This is a multi-line comment. 
It can span multiple lines. 
"""  
 
def add_numbers(a, b):
     """Adds two numbers and returns the result."""
     print(f"Adding numbers...  {a}  and {b}, result:  { a + b}")
     
     return a + b
 
 
add_numbers(5, 10) # Output: 15
def divide_numbers(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        print(f"Error: Division by zero is not allowed. ,{ a}, {b}, result: None")
        return None
    else:
        result = a / b
        print(f"Dividing numbers... ,{ a}, {b}, result: {result}")
        return result

# Test cases
divide_numbers(5, 10)  # Output: Dividing numbers... 5 10 result: 0.5
divide_numbers(30, 0) # Output: Error: Division by zero is not allowed.