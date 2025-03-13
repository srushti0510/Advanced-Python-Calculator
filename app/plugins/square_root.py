import math
import cmath
from app.history import save_single_input_history

def execute():
    try:
        number = float(input("Enter a number to calculate the square root: "))
        
        if number < 0:
            # Use cmath for negative numbers
            complex_result = cmath.sqrt(number)
            # Format output EXACTLY as "2j" not "2.0j" - use string formatting
            result_str = f"{int(complex_result.imag)}j"
            print(f"The square root of {number} is {result_str}")
            save_single_input_history('square_root', number, result_str)
        else:
            result = math.sqrt(number)
            print(f"The square root of {number} is {result}")
            save_single_input_history('square_root', number, result)
            
    except ValueError:
        print("Error: Please enter a valid number")
    except Exception as e:
        print(f"Error: {e}")