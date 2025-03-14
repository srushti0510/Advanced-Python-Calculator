import pandas as pd  # type: ignore
import os

HISTORY_FILE = 'data/history.csv'

def load_history():
    """Loads calculation history from a CSV file."""
    if os.path.exists(HISTORY_FILE):
        print(f"History file found: {HISTORY_FILE}")
        if os.path.getsize(HISTORY_FILE) > 0:
            print("History file is not empty, loading data.")
            return pd.read_csv(HISTORY_FILE)
        else:
            print("History file is empty.")
            return pd.DataFrame(columns=['operation', 'x', 'y', 'result'])
    else:
        print("History file not found, creating a new one.")
        os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)  # Create data directory if it doesn't exist
        return pd.DataFrame(columns=['operation', 'x', 'y', 'result'])

def save_history(operation, x, y, result):
    """Saves a new calculation to the CSV history file."""
    
    # Check if result is valid (not None or invalid type)
    if result is None:
        raise ValueError("Result cannot be None.")
    
    if not isinstance(result, (int, float)):  # Ensure result is a valid number
        raise ValueError("Result must be a valid number (int or float).")
    
    # Load current history (could be empty if no data exists)
    history = load_history()

    # Debugging: Show what is being saved
    print(f"Saving new history record: {operation} with x={x}, y={y}, result={result}")
    
    # Create a new record
    new_record = pd.DataFrame([[operation, x, y, result]], columns=['operation', 'x', 'y', 'result'])
    print(f"New record to append:\n{new_record}")  # Debugging print
    
    # Use pd.concat() instead of append
    history = pd.concat([history, new_record], ignore_index=True)
    
    # Debugging: Print updated history before saving
    print(f"Updated history to save:\n{history}")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    
    # Save the updated history to the CSV file
    history.to_csv(HISTORY_FILE, index=False)
    print(f"History saved successfully to {HISTORY_FILE}")

def clear_history():
    """Clears the entire history (empties the CSV file without deleting it)."""
    if os.path.exists(HISTORY_FILE):
        # Create an empty DataFrame with the same columns
        empty_history = pd.DataFrame(columns=['operation', 'x', 'y', 'result'])
        
        # Save the empty DataFrame back to the CSV file
        empty_history.to_csv(HISTORY_FILE, index=False)
        print(f"History has been cleared. {HISTORY_FILE} is now empty.")
    else:
        print(f"History file {HISTORY_FILE} does not exist.")

def print_history():
    """Displays the calculation history."""
    history = load_history()
    if history.empty:
        print("No history found.")
    else:
        print("Calculation History:")
        print(history)

def delete_history():
    """Deletes all history records from the CSV file."""
    if os.path.exists(HISTORY_FILE):
        empty_history = pd.DataFrame(columns=['operation', 'x', 'y', 'result'])
        empty_history.to_csv(HISTORY_FILE, index=False)  # Clear the CSV file
        print(f"History has been deleted. {HISTORY_FILE} is now empty.")
    else:
        print(f"History file {HISTORY_FILE} does not exist.")

def delete_specific_history(operation):
    """Deletes specific records based on operation."""
    history = load_history()  # Load current history

    # Filter out the operation we want to delete
    updated_history = history[history['operation'] != operation]

    # Check if the operation exists in the history
    if len(updated_history) == len(history):
        # If no records were deleted, print that no records for the operation were found
        print(f"No records found for operation: {operation}")
    else:
        # If records are deleted, save the updated history and print a success message
        updated_history.to_csv(HISTORY_FILE, index=False)
        print(f"Deleted all records for operation: {operation}")


        
# New function for single-input operations
def save_single_input_history(operation, x, result):
    """Saves a calculation with only one input to history."""
    # For single input operations, we'll use None for the y value
    save_history(operation, x, None, result)
