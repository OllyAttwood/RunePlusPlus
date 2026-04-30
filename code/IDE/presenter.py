from output_redirect import OutputRedirector
import sys
import builtins

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
        self.view.register_stop_callback(self.on_stop_button_click)

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
            self.view.set_title(file_path)

    def on_save_as_button_click(self):
        """
        Gets the text from the code window, gets the desired save location, then saves
        it as the current file
        """
        file_contents = self.view.get_code_window_text()
        file_path = self.view.request_save_path()
        if file_path:
            self.model.save_to_file(file_path, file_contents)
            self.view.set_title(file_path)

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
        try:
            self.view.set_execution_buttons_state(run_enabled=False)
            self.model.run_code_from_current_file(
                self.view.get_input,
                self.view.append_to_console,
                self.on_code_execution_finished
            )
        except FileNotFoundError:
            self.view.display_error_message(
                "No current file to run (file must be saved/opened)!"
            )
            self.view.set_execution_buttons_state(run_enabled=True)
        except Exception as err:
            self.view.display_error_message(f"Error running code: {err}")

    def on_code_execution_finished(self):
        """Called when subprocess finishes - updates UI buttons (run/stop)"""
        # after() ensures that the method is called on the UI thread
        self.view.after(
            0,
            lambda: self.view.set_execution_buttons_state(run_enabled=True)
        )

    def on_stop_button_click(self):
        """Stops the currently running code execution"""
        self.model.stop_code_execution()
        self.view.cancel_pending_input()  # Unblock any thread waiting for input
        self.view.set_execution_buttons_state(run_enabled=True)

    def gui_input(self, prompt):
        """Wrapper for new input function"""
        return self.view.get_input(prompt)
