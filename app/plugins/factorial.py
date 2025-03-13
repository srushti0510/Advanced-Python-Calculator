from app.history import save_single_input_history

def execute():
    """Function to calculate the factorial of a number."""
    try:
        number = int(input("Enter a number to calculate its factorial: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
            return
        
        result = 1
        for i in range(1, number + 1):
            result *= i
            
        print(f"The factorial of {number} is {result}")
        
        # Save to history
        save_single_input_history('factorial', number, result)
    except Exception as e:
        print(f"Error: {e}")