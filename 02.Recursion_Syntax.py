# syntax with recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
# Example usage of the factorial function
print(factorial(5))  # Output: 120

# Function with recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  
# Example usage of the fibonacci function
print(fibonacci(6))  # Output: 8

