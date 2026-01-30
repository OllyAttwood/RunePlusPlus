from output_redirect import OutputRedirector
import sys
import builtins
from threading import Thread
import subprocess
import os

class Presenter:
    """The presenter class to co-ordinate the view with the real functionality"""

    def __init__(self, view, model):
        self.view = view
        self.model = model

        # Setup button callbacks
        self.view.register_open_file_callback(self.on_open_file_button_click)
        self.view.register_save_as_callback(self.on_save_as_button_click)
        self.view.register_save_callback(self.on_save_button_click)
        self.view.register_run_callback(self.on_run_button_click)

        # Setup output redirect from terminal to IDE console
        output_redirector = OutputRedirector(self.view.append_to_console)
        sys.stdout = output_redirector
        sys.stderr = output_redirector

        # Setup input redirect from terminal to IDE console
        builtins.input = self.gui_input

    def on_open_file_button_click(self):
        """
        Gets the desired file location, gets its contents, then displays it in the view
        """
        file_path = self.view.request_open_path()

        if file_path:
            file_contents = self.model.open_file(file_path)
            self.view.set_code_window_text(file_contents)

    def on_save_as_button_click(self):
        """
        Gets the text from the code window, gets the desired save location, then saves
        it as the current file
        """
        file_contents = self.view.get_code_window_text()
        file_path = self.view.request_save_path()
        if file_path:
            self.model.save_to_file(file_path, file_contents)

    def on_save_button_click(self):
        """Gets the text from the code window, then saves it as the current file"""
        file_contents = self.view.get_code_window_text()
        try:
            self.model.save_to_current_file(file_contents)
        except ValueError as err:
            self.view.display_error_message(err)

    def on_run_button_click(self):
        """Runs the code in the current file"""
        self.view.clear_console()
        self._run_user_code_in_subprocess()

    def _run_user_code_in_subprocess(self):
        """
        Runs the user code in a subprocess. This is used instead of a thread so that the 
        user code can be killed during execution without crashing the UI. Also is more 
        isolated than threads/multiprocessing.
        """
        try:
            if not self.model.current_file_name:
                raise FileNotFoundError(
                    "No current file to run (file must be saved/opened)!"
                ) 

            # Run the user's code in a separate process to keep UI unblocked
            python_exe = sys.executable
            run_file_path = self._get_run_file_path() # Deals with /../
            run_subprocess = subprocess.Popen(
                [python_exe, run_file_path, self.model.current_file_name],
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1, # Line buffering
                universal_newlines=True # Needed for backwards compatibility
            )

            run_subprocess_thread = Thread(
                target=self._read_subprocess_output,
                args=(run_subprocess,)
            )
            run_subprocess_thread.start()

        except FileNotFoundError as err:
            self.view.display_error_message(
                "No current file to run (file must be saved/opened)!"
            )
        except Exception as err:
            self.view.display_error_message(
                f"Error running code: {err}"
            )

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

    def _read_subprocess_output(self, subproc):
        """ 
        Reads the output from a subprocess, and handles input requests from that 
        subprocess by passing it on to the UI, then passing the user input back to the 
        subprocess
        """
        INPUT_REQUEST_TAG = "<INPUT_REQUEST>"

        for line in iter(subproc.stdout.readline, ""): # Stops when "" is provided
            if line:
                # If input request
                if line.startswith(INPUT_REQUEST_TAG):
                    prompt = line[len(INPUT_REQUEST_TAG):].rstrip("\n\r")
                    user_input = self.view.get_input(prompt)
                    subproc.stdin.write(user_input + "\n")
                    subproc.stdin.flush()
                else: # If regular output
                    self.view.append_to_console(line)

        subproc.stdout.close()
        subproc.stdin.close()
        subproc.wait()

    def gui_input(self, prompt):
        """Wrapper for new input function"""
        return self.view.get_input(prompt)
