import math
import cmath
from app.history import save_single_input_history

def execute():
    try:
        number_input = input("Enter a number to calculate the square root: ")
        
        # Check if the input is a valid number
        try:
            number = float(number_input)
        except ValueError:
            print("Error: Invalid input for square root. Please enter a valid number.")
            return
        
        if number < 0:
            # Use cmath for negative numbers to handle complex square roots
            complex_result = cmath.sqrt(number)
            result_str = f"{int(complex_result.imag)}j" if complex_result.imag.is_integer() else f"{complex_result.imag}j"
            print(f"The square root of {number} is {result_str}")
            save_single_input_history('square_root', number, result_str)
        else:
            result = math.sqrt(number)
            print(f"The square root of {number} is {result}")
            save_single_input_history('square_root', number, result)
            
    except Exception as e:
        print(f"Error: {e}")
