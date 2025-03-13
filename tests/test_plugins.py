from app.plugins.square_root import execute as square_root_execute
from app.plugins.factorial import execute as factorial_execute

def test_square_root():
    # Simulating user input for square root
    # Use a mock input if required, or test the functionality directly
    # E.g., Use pytest's monkeypatch to simulate user input
    
    try:
        square_root_execute()  # Calls the square root plugin's execute method
    except Exception as e:
        assert False, f"Error in square root plugin: {e}"

def test_factorial():
    # Simulating user input for factorial
    try:
        factorial_execute()  # Calls the factorial plugin's execute method
    except Exception as e:
        assert False, f"Error in factorial plugin: {e}"
