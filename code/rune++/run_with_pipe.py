""" 
Wrapper for the run.py file, allowing it to be run as a subprocess with a pip for
two-way communication with the main process
"""
import sys
import builtins
import run

def _pipe_input(prompt):
    """
    Function to override the built-in input function, sending an input request from the
    user code subprocess to the main process via a pipe. Waits for the given input from 
    the main process (UI) then returns it.
    """
    sys.stdout.write(f"<INPUT_REQUEST>{prompt}\n")
    sys.stdout.flush()

    user_input = sys.stdin.readline()

    if user_input:
        return user_input.rstrip('\n\r')
    else:
        return ""
    
# Override the built-in input function
builtins.input = _pipe_input

# Run the user code
run.run_from_command_line()