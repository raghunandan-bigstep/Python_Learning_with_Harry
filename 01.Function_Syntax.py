# Syntax of Functions in Python

# write a python function to greet a user with "Good Day" 
def greet(name):
    """Prints a personalized greeting message"""
    print(f"Good Day, {name}!")
    
# Example usage of the greet function
greet("Alice")

# There are two types of functions in Python:
'''1. Built-in functions: These are functions that are already defined in Python, such
as `print()`, `len()`, and `type()`. They can be used directly without any additional definition.'''

'''2. User-defined functions: These are functions that you define yourself using the `def`
 keyword. User-defined functions can take parameters, return values, and have their own'''
 
 # function with arguments
def greet(name, age):
     """Prints a personalized greeting message with age"""
     print(f"Hello, {name}! You are {age} years old.")

# Example usage of the greet function with arguments
greet("Alice", 30)

# Function with default parameter
def greet(name = "World"):
    """Prints a personalized greeting message"""
    print(f"Hello, {name}!")
    
# Example usage of the greet function with default parameter
greet("Alice")
greet()  # Calls the function with the default parameter

# Function with multiple parameters
def add_numbers(a, b):
    """Returns the sum of two numbers"""
    return a + b

# Example usage of the add_numbers function
print(add_numbers(5, 7))

# Function with variable number of arguments
def sum_all(*args):
    """Returns the sum of all arguments"""
    return sum(args)

# Example usage of the sum_all function
print(sum_all(1, 2, 3, 4, 5))

# Function with keyword arguments
def greet(name, age):
    """Prints a personalized greeting message"""
    print(f"Hello, {name}! You are {age} years old.")

# Example usage of the greet function with keyword arguments
greet(name="Alice", age=30)

# Function with keyword arguments and default values
def greet(name="World", age=0):
    """Prints a personalized greeting message with default values"""
    print(f"Hello, {name}! You are {age} years old.")

# Example usage of the greet function with keyword arguments and default values
greet(name="Alice", age=30)
greet()  # Calls the function with the default values



# Function with return statement
def greet(name):
    """Returns a personalized greeting message"""
    return f"Hello, {name}!"

# Example usage of the greet function with return statement
print(greet("Alice"))

# Function with multiple return statements
print("This function has multiple return statements.")
def greet(name):
    """Returns a personalized greeting message with multiple return statements"""
    return f"Hello, {name}!"
    return f"Goodbye, {name}!"  # This second return statement will never be executed

# Example usage of the greet function with multiple return statements
print(greet("Alice"))




# Function with nested functions
def outer_function():
    """Defines a nested function"""
    def inner_function():
        """Returns a message from the inner function"""
        return "Hello from the inner function!"    
    return inner_function()
# Example usage of the outer_function with nested functions
print(outer_function())
