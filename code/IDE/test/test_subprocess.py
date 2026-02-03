"""
Tests for the user code subprocess related functions.

If the command "pytest" doesn't work (as it didn't for me), use
"python -m pytest" instead.

Run the command from the code/IDE directory.

See https://www.tutorialspoint.com/pytest/index.htm for more help
"""

import pytest
import os
from IDE_functions import IDE_Functions

def test_get_run_file_path():
    model = IDE_Functions()

    path = model._get_run_file_path()

    # Check that the path is absolute
    assert os.path.isabs(path), "Path should be absolute"
    
    # Check that it ends with the expected filename
    assert path.endswith("run_with_pipe.py"), "Path should end with 'run_with_pipe.py'"
    
    # Check that the file actually exists
    assert os.path.exists(path), f"File should exist at: {path}"
    
    # Check that it's a file, not a directory
    assert os.path.isfile(path), f"Path should be a file: {path}"
