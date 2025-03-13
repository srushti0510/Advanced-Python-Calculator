import pandas as pd
import os

history_file = 'data/history.csv'

def load_history():
    """Loads calculation history from a CSV file."""
    if os.path.exists(history_file):
        print(f"History file found: {history_file}")
        if os.path.getsize(history_file) > 0:
            print("History file is not empty, loading data.")
            return pd.read_csv(history_file)
        else:
            print("History file is empty.")
            return pd.DataFrame(columns=['operation', 'x', 'y', 'result'])
    else:
        print("History file not found, creating a new one.")
        return pd.DataFrame(columns=['operation', 'x', 'y', 'result'])

def save_history(operation, x, y, result):
    """Saves a new calculation to the CSV history file."""
    history = load_history()  # Load current history (could be empty if no data exists)
    
    # Debugging: Show what is being saved
    print(f"Saving new history record: {operation} with x={x}, y={y}, result={result}")
    
    # Create a new record
    new_record = pd.DataFrame([[operation, x, y, result]], columns=['operation', 'x', 'y', 'result'])
    print(f"New record to append:\n{new_record}")  # Debugging print
    
    # Use pd.concat() instead of append
    history = pd.concat([history, new_record], ignore_index=True)
    
    # Debugging: Print updated history before saving
    print(f"Updated history to save:\n{history}")
    
    # Save the updated history to the CSV file
    history.to_csv(history_file, index=False)
    print(f"History saved successfully to {history_file}")

def clear_history():
    """Clears the entire history (empties the CSV file without deleting it)."""
    if os.path.exists(history_file):
        # Create an empty DataFrame with the same columns
        empty_history = pd.DataFrame(columns=['operation', 'x', 'y', 'result'])
        
        # Save the empty DataFrame back to the CSV file
        empty_history.to_csv(history_file, index=False)
        print(f"History has been cleared. {history_file} is now empty.")
    else:
        print(f"History file {history_file} does not exist.")

def print_history():
    """Displays the calculation history."""
    history = load_history()
    if history.empty:
        print("No history found.")
    else:
        print("Calculation History:")
        print(history)
