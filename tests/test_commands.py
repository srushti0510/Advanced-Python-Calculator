from unittest.mock import patch
from app.commands import CalculatorREPL
from app.history import save_history, clear_history, load_history

# Combined invalid arithmetic input test
def test_invalid_arithmetic_input(capsys):
    invalid_inputs = [
        ('a b', 'Error: could not convert string to float'),  # Invalid addition
        ('10 x', 'Error: could not convert string to float'),  # Invalid subtraction
        ('3 y', 'Error: could not convert string to float'),  # Invalid multiplication
        ('12 z', 'Error: could not convert string to float')   # Invalid division
    ]
    
    for input_value, expected_error in invalid_inputs:
        with patch('builtins.input', return_value=input_value):
            calculator = CalculatorREPL()
            calculator.do_add(input_value) if 'a' in input_value else \
                calculator.do_subtract(input_value) if 'x' in input_value else \
                calculator.do_multiply(input_value) if 'y' in input_value else \
                calculator.do_divide(input_value)
            
            captured = capsys.readouterr()
            assert expected_error in captured.out  # Check for the expected error message

# Test for division by zero
def test_division_by_zero(capsys):
    with patch('builtins.input', return_value='12 0'):  # Division by zero
        calculator = CalculatorREPL()
        calculator.do_divide('12 0')
        captured = capsys.readouterr()
        assert "Error: Cannot divide by zero" in captured.out  # Ensure division by zero is handled

def test_menu_navigation(capsys):
    valid_choices = ['1', '2', '6']  # Valid choices (Arithmetic, View History, Exit)
    
    for choice in valid_choices:
        with patch('builtins.input', return_value=choice):
            calculator = CalculatorREPL()
            calculator.default(choice)  # Simulate selecting a valid menu option
            
            captured = capsys.readouterr()
            
            # Validate the output based on the chosen menu option
            if choice == '1':  # For Arithmetic menu choice
                assert "Select an arithmetic operation:" in captured.out
            elif choice == '2':  # For View History menu choice
                assert "Calculation History:" in captured.out
            elif choice == '6':  # For Exit choice
                assert "Exiting calculator... Thank you!" in captured.out

    # Test for invalid menu choice (should print error message)
    with patch('builtins.input', return_value='99'):  # Invalid choice
        calculator = CalculatorREPL()
        calculator.default('99')  # Simulate invalid input
        captured = capsys.readouterr()
        assert "Invalid choice, please select a valid option." in captured.out  # Ensure error message is printed


# Test for plugin loading with invalid choice
def test_load_plugin_invalid(capsys):
    with patch('builtins.input', return_value='99'), patch('app.commands.list_plugins', 
                                            return_value=['square_root', 'factorial']):
        calculator = CalculatorREPL()
        calculator.load_plugins()
        captured = capsys.readouterr()
        assert "Invalid plugin choice." in captured.out  # Ensure invalid plugin choice is handled

# Test for no available plugins
def test_no_plugins_available(capsys):
    with patch('app.commands.list_plugins', return_value=[]):  # No plugins available
        calculator = CalculatorREPL()
        calculator.load_plugins()  # This should handle the case where no plugins are available
        captured = capsys.readouterr()
        # Ensure appropriate message is printed
        assert "No advanced features available." in captured.out  

# Test for deleting specific history (when the operation doesn't exist)
def test_delete_specific_history_not_found(capsys):
    save_history('add', 5, 3, 8)  # Add a history record for 'add' operation
    
    with patch('builtins.input', return_value='subtract'):  # Trying to delete non-existent operation
        calculator = CalculatorREPL()
        calculator.delete_specific_history_prompt()  # Simulate the delete specific history prompt
        
        captured = capsys.readouterr()
        assert "No records found for operation: subtract" in captured.out

# Test for viewing history when history is empty
def test_view_history_empty(capsys):
    clear_history()  # Ensure history is empty
    calculator = CalculatorREPL()
    calculator.view_history()  # Simulate the 'view history' operation
    captured = capsys.readouterr()
    assert "No history found." in captured.out  # Should display no history message

# Test for clearing history
def test_clear_history(capsys):
    save_history('add', 5, 3, 8)  # Simulate adding to history
    clear_history()  # Directly call the function to clear history
    captured = capsys.readouterr()
    assert "History has been cleared." in captured.out  # Ensure the clear history message is printed

# Test for deleting all history
def test_delete_all_history(capsys):
    save_history('add', 5, 3, 8)
    save_history('subtract', 10, 4, 6)
    
    with patch('builtins.input', return_value='1'):  # Simulate delete all history
        calculator = CalculatorREPL()
        calculator.delete_history_prompt()  # Simulate the delete history prompt
        captured = capsys.readouterr()
        assert "History has been deleted." in captured.out  # Ensure the delete message appears

    # Verify history is cleared
    history = load_history()
    assert history.empty  # History should be empty after deletion

# Test for invalid addition (non-numeric input)
def test_invalid_addition(capsys):
    with patch('builtins.input', return_value='a b'):  # Invalid input (letters instead of numbers)
        calculator = CalculatorREPL()
        calculator.do_add('a b')  # Simulate addition with invalid input
        captured = capsys.readouterr()
        assert "Error: could not convert string to float" in captured.out  # Ensure error message is printed

# Test for invalid subtraction (non-numeric input)
def test_invalid_subtraction(capsys):
    with patch('builtins.input', return_value='10 x'):  # Invalid input
        calculator = CalculatorREPL()
        calculator.do_subtract('10 x')  # Simulate subtraction with invalid input
        captured = capsys.readouterr()
        assert "Error: could not convert string to float" in captured.out

# Test for invalid multiplication (non-numeric input)
def test_invalid_multiplication(capsys):
    with patch('builtins.input', return_value='3 y'):  # Invalid input
        calculator = CalculatorREPL()
        calculator.do_multiply('3 y')  # Simulate multiplication with invalid input
        captured = capsys.readouterr()
        assert "Error: could not convert string to float" in captured.out

# Test for invalid division (non-numeric input)
def test_invalid_division(capsys):
    with patch('builtins.input', return_value='12 z'):  # Invalid input
        calculator = CalculatorREPL()
        calculator.do_divide('12 z')  # Simulate division with invalid input
        captured = capsys.readouterr()
        assert "Error: could not convert string to float" in captured.out

# Test for loading plugins with square root
def test_load_square_root_plugin(capsys):
    # Mock the list_plugins function to return a list of available plugins
    with patch('builtins.input', return_value='1'), patch('app.commands.list_plugins', return_value=['square_root']):
        
        # Mock the behavior of the square_root plugin
        def mock_square_root_plugin(name):
            if name == 'square_root':
                print("The square root of 4 is 2.0")
        
        # Patch the load_plugin function to use the mock function
        with patch('app.commands.load_plugin', side_effect=mock_square_root_plugin):
            # Create a CalculatorREPL instance and run the plugin loading process
            calculator = CalculatorREPL()
            calculator.load_plugins()  # This should trigger the plugin selection and execution

            # Capture the printed output from the plugin
            captured = capsys.readouterr()

            # Check if the expected output is in the captured stdout
            assert "The square root of 4 is 2.0" in captured.out  # Ensure correct plugin output is printed

# Test for loading plugins with factorial
def test_load_factorial_plugin(capsys):
    # Now test for factorial plugin selection
    with patch('builtins.input', return_value='2'), patch('app.commands.list_plugins', return_value=['square_root', 'factorial']):
        
        # Mock the behavior of the factorial plugin
        def mock_factorial_plugin(name):
            if name == 'factorial':
                print("The factorial of 5 is 120")
        
        # Patch the load_plugin function to use the mock function
        with patch('app.commands.load_plugin', side_effect=mock_factorial_plugin):
            # Create a CalculatorREPL instance and run the plugin loading process
            calculator = CalculatorREPL()
            calculator.load_plugins()  # This should trigger the plugin selection and execution

            # Capture the printed output from the plugin
            captured = capsys.readouterr()

            # Check if the expected output is in the captured stdout
            assert "The factorial of 5 is 120" in captured.out  # Ensure correct plugin output is printed
