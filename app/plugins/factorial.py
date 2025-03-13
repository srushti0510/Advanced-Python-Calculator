# app/plugins/factorial.py
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
    except Exception as e:
        print(f"Error: {e}")
