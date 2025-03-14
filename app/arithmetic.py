def add(x, y):
    """
    Add two numbers.
    """
    return x + y

def subtract(x, y):
    """
    Subtract two numbers.
    """
    return x - y

def multiply(x, y):
    """
    Multiply two numbers.
    """
    return x * y

def divide(x, y):
    """
    Divide one number with another.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
