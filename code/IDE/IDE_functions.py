import sys
import os
from threading import Thread
import subprocess

# Importing module to run code here, which is in a parallel directory, therefore needs
# to be imported differently (also the directory 'rune++' contains invalid characters
# for regular importing)
run_module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rune++'))
sys.path.insert(0, run_module_path)
import run

class IDE_Functions:
    """
    Class which serves as the model component of the MVP pattern. This contains all the
    functionality and attributes needed for the IDE.
    """

    def __init__(self):
        self.current_file_name = ""
        self.run_subprocess = None
        self._stop_requested = False

    def open_file(self, file_path):
        """
        Returns the text from the file at the given location, also updates
        current_file_name
        """
        with open(file_path) as open_file:
            file_contents = open_file.read()

        self.current_file_name = file_path

        return file_contents

    def save_to_file(self, file_path, text_to_save):
        """
        Saves the text to the given file location, also updates current_file_name
        """
        with open(file_path, "w") as open_file:
            open_file.write(text_to_save)

        self.current_file_name = file_path

    def save_to_current_file(self, text_to_save):
        """
        Saves the text to the current file location, also updates current_file_name
        """
        if self.current_file_name == "" or self.current_file_name is None:
            raise ValueError("No current file to save to!")

        self.save_to_file(self.current_file_name, text_to_save)

    def run_code_from_current_file(self, get_input_callback, return_output_callback):
        """
        Runs the user code in a subprocess. This is used instead of a thread so that the 
        user code can be killed during execution without crashing the UI. Also is more 
        isolated than threads/multiprocessing.
        """
        if not self.current_file_name:
            raise FileNotFoundError(
                "No current file to run (file must be saved/opened)!"
            )

        self._stop_requested = False

        # Run the user's code in a separate process to keep UI unblocked
        python_exe = sys.executable
        run_file_path = self._get_run_file_path() # Deals with /../
        self.run_subprocess = subprocess.Popen(
            [python_exe, run_file_path, self.current_file_name],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1, # Line buffering
            universal_newlines=True # Needed for backwards compatibility
        )

        run_subprocess_thread = Thread(
            target=self._read_subprocess_output,
            args=(self.run_subprocess, get_input_callback, return_output_callback)
        )
        run_subprocess_thread.start()

    def _get_run_file_path(self):
        """
        Returns the absolute path of the module which runs the user code using a pipe 
        for communication.
        """
        run_file_path = os.path.dirname(os.path.abspath(__file__))
        run_file_path = os.path.join(
            run_file_path, "..",
            "rune++",
            "run_with_pipe.py"
        )
        run_file_path = os.path.abspath(run_file_path)

        return run_file_path

    def _read_subprocess_output(
        self,
        subproc,
        get_input_callback,
        return_output_callback
    ):
        """ 
        Reads the output from a subprocess, and handles input requests from that 
        subprocess by passing it on to the UI, then passing the user input back to the 
        subprocess
        """
        INPUT_REQUEST_TAG = "<INPUT_REQUEST>"

        try:
            for line in iter(subproc.stdout.readline, ""): # Stops when "" is provided
                if self._stop_requested:
                    break
                if line:
                    # If input request
                    if line.startswith(INPUT_REQUEST_TAG):
                        prompt = line[len(INPUT_REQUEST_TAG):].rstrip("\n\r")
                        user_input = get_input_callback(prompt)
                        # Check if stop was requested while waiting for input
                        if self._stop_requested:
                            break
                        subproc.stdin.write(user_input + "\n")
                        subproc.stdin.flush()
                    else: # If regular output
                        return_output_callback(line)
        except (BrokenPipeError, OSError):
            # Subprocess was terminated - exit gracefully.
            # This can happen if the stop button is clicked while the subprocess is 
            # waiting for input - unlikely but possible
            pass

        subproc.stdout.close()
        subproc.stdin.close()
        subproc.wait()

    def stop_code_execution(self):
        """Stops the currently running user code subprocess"""
        self._stop_requested = True
        if self.run_subprocess and self.run_subprocess.poll() is None:
            self.run_subprocess.terminate()
            self.run_subprocess.wait() # Clean up subprocess resources
            self.run_subprocess = None
