import math
from app.history import save_single_input_history

def execute():
    try:
        num = int(input("Enter a number to calculate factorial: "))
        
        if num < 0:
            print("Factorial is not defined for negative numbers.")
            return
        
        result = math.factorial(num)
        print(f"The factorial of {num} is {result}")
        
        # Save to history
        save_single_input_history('factorial', num, result)
        
    except ValueError:
        # Update this message to match exactly what the test expects
        print("Error: Invalid input for factorial. Please enter a valid number.")
    except Exception as e:
        print(f"Error: {e}")