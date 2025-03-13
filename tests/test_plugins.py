# type: ignore
import pytest
import math
from unittest.mock import patch, ANY
import importlib
import os
from app.plugins import list_plugins, load_plugin

# Test for square_root functionality
def test_square_root_calculation():
    # Import the function directly to test the calculation logic
    from app.plugins.square_root import execute
    
    # Mock the input and print functions
    with patch('builtins.input', return_value='9'), patch('builtins.print') as mock_print:
        execute()
        # Check if the correct result was printed
        mock_print.assert_any_call('The square root of 9.0 is 3.0')

def test_square_root_error():
    from app.plugins.square_root import execute
    
    # Test with invalid input (negative number should work but produce a complex number)
    with patch('builtins.input', return_value='-4'), patch('builtins.print') as mock_print:
        execute()
        # The square root of -4 is a complex number (should print this properly)
        mock_print.assert_any_call('The square root of -4.0 is 2j')  # Handling complex results for negative numbers

def test_square_root_invalid_input():
    """Test for invalid input in square_root (non-numeric input)."""
    from app.plugins.square_root import execute
    
    with patch('builtins.input', return_value='abc'), patch('builtins.print') as mock_print:
        execute()
        mock_print.assert_any_call('Error: Invalid input for square root. Please enter a valid number.')

# Test for factorial functionality
def test_factorial_calculation():
    from app.plugins.factorial import execute
    
    # Test with valid input
    with patch('builtins.input', return_value='5'), patch('builtins.print') as mock_print:
        execute()
        # Check if the correct result was printed
        mock_print.assert_any_call('The factorial of 5 is 120')

def test_factorial_zero():
    from app.plugins.factorial import execute
    
    # Test with zero
    with patch('builtins.input', return_value='0'), patch('builtins.print') as mock_print:
        execute()
        # The factorial of 0 is 1
        mock_print.assert_any_call('The factorial of 0 is 1')

def test_factorial_negative():
    from app.plugins.factorial import execute
    
    # Test with negative number
    with patch('builtins.input', return_value='-5'), patch('builtins.print') as mock_print:
        execute()
        # Check if the correct error message was printed
        mock_print.assert_any_call('Factorial is not defined for negative numbers.')

def test_factorial_invalid_input():
    """Test for invalid input in factorial (non-numeric input)."""
    from app.plugins.factorial import execute
    
    with patch('builtins.input', return_value='abc'), patch('builtins.print') as mock_print:
        execute()
        mock_print.assert_any_call('Error: Invalid input for factorial. Please enter a valid number.')

# Test plugin listing functionality
def test_list_plugins():
    # This assumes your plugins directory has at least square_root.py and factorial.py
    plugins = list_plugins()
    assert 'square_root' in plugins
    assert 'factorial' in plugins

# Test plugin loading functionality
def test_load_plugin():
    # Create a mock module with an execute method
    mock_module = type('mock_module', (), {'execute': lambda: None})
    
    # Test loading a valid plugin
    with patch('importlib.import_module', return_value=mock_module) as mock_import:
        load_plugin('square_root')
        mock_import.assert_called_once_with('app.plugins.square_root')
    
    # For the second part, since we know it prints an error instead of raising an exception
    with patch('builtins.print') as mock_print:
        load_plugin('non_existent_plugin')
        expected_msg = "Error loading plugin non_existent_plugin: No module named 'app.plugins.non_existent_plugin'"
        any_call_found = False
        for call in mock_print.call_args_list:
            args, _ = call
            if args and expected_msg in args[0]:
                any_call_found = True
                break
        assert any_call_found, f"Expected error message not found in print calls: {expected_msg}"
