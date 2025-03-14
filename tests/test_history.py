import os
import pytest
import pandas as pd
from app.history import load_history, save_history, clear_history

history_file = 'data/history.csv'

@pytest.fixture
def setup_history_file():
    """Fixture to reset the history file before each test."""
    # Clear history before running tests
    clear_history()
    yield
    # Cleanup after tests (optional, if you need to clear history after tests)
    clear_history()

def test_load_history_empty(setup_history_file):
    """Test loading history when no history exists (empty file)."""
    history = load_history()
    assert history.empty  # Should be an empty DataFrame
    assert list(history.columns) == ['operation', 'x', 'y', 'result']

def test_save_history(setup_history_file):
    """Test saving history to the CSV file."""
    # Save a new record
    save_history('add', 5, 3, 8)
    
    # Load the history to check if it's saved
    history = load_history()
    assert not history.empty
    assert len(history) == 1  # Should have 1 record
    assert history.iloc[0]['operation'] == 'add'
    assert history.iloc[0]['x'] == 5
    assert history.iloc[0]['y'] == 3
    assert history.iloc[0]['result'] == 8

def test_clear_history(setup_history_file):
    """Test clearing the history."""
    save_history('add', 5, 3, 8)
    
    # Clear the history
    clear_history()
    
    # Load the history and check if it's empty
    history = load_history()
    assert history.empty  # Should be empty after clearing

def test_history_after_multiple_operations(setup_history_file):
    """Test saving and loading multiple operations."""
    save_history('add', 5, 3, 8)
    save_history('subtract', 10, 4, 6)
    
    # Load the history and verify the records
    history = load_history()
    assert len(history) == 2
    assert history.iloc[0]['operation'] == 'add'
    assert history.iloc[1]['operation'] == 'subtract'

def test_invalid_save(setup_history_file):
    """Test saving invalid history (e.g., missing values)."""
    with pytest.raises(ValueError):
        save_history('add', 5, 3, None)  # Try saving invalid result (None)


def test_save_invalid_result(setup_history_file):
    """Test saving history with invalid result (e.g., None or non-numeric result)."""
    with pytest.raises(ValueError):
        save_history('add', 5, 3, None)  # Invalid result
    with pytest.raises(ValueError):
        save_history('add', 5, 3, 'invalid')  # Invalid result type (non-numeric)

def test_clear_empty_history(setup_history_file):
    """Test clearing an already empty history."""
    clear_history()
    history = load_history()
    assert history.empty  # Should still be empty after clearing



