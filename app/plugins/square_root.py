import math

def execute():
    try:
        number = float(input("Enter a number to calculate the square root: "))
        result = math.sqrt(number)
        print(f"The square root of {number} is {result}")
    except Exception as e:
        print(f"Error: {e}")
