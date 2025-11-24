from output_redirect import OutputRedirector
import sys
import builtins
from threading import Thread

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
        try:
            # Run the user's code in a separate thread to keep UI unblocked
            user_code_thread = Thread(
                target=self.model.run_code_from_current_file,
                daemon=True
            )
            user_code_thread.start()
        except FileNotFoundError as err:
            self.view.display_error_message(
                "No current file to run (file must be saved/opened)!"
            )

    def gui_input(self, prompt):
        """Wrapper for new input function"""
        return self.view.get_input(prompt)
