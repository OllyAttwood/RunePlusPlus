import customtkinter as ctk
from tkinter import *
import tkinter.filedialog
import menu_bar
import keyboard
from messagebox import MessageBox
import threading

# Ignore CTkButton warning when using a PhotoImage
import warnings
warnings.filterwarnings("ignore", message="CTkButton Warning: Given image is not CTkImage*")

class UI(ctk.CTk):
    """The main UI Window"""

    def __init__(self):
        # Window setup
        super().__init__()
        self.title("Rune++ IDE")
        self.attributes("-zoomed", True) # Full-screen
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        text_size = 15
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # Button callbacks
        self.open_file_callback = None
        self.save_as_callback = None
        self.save_callback = None
        self.run_callback = None

        # Menu bar
        self.menu = menu_bar.MenuBar(
            bg="grey",
            activebackground="#36454F"
        )
        self.menu.register_open_file_callback(self.open_file_command)
        self.menu.register_save_as_callback(self.save_as_command)
        self.menu.register_save_callback(self.save_command)
        self.menu.register_run_callback(self.run_command)
        self.config(menu=self.menu)

        # Input() function thread handling, to replace the builtin function
        self.input_event = threading.Event()
        self.input_value = None

        # Text box
        self.text_box = ctk.CTkTextbox(self, font=(None, text_size))
        self.text_box.grid(row=0, column=0, columnspan=2, sticky="nesw")

        # Keyboard
        self.keyboard_frame = keyboard.KeyboardFrame(self)
        self.keyboard_frame.grid(row=1, column=0, columnspan=2)

        # Console log
        console_log_label = ctk.CTkLabel(self, text="Console")
        console_log_label.grid(row=2, column=0, sticky="w")
        self.console_log = ctk.CTkTextbox(self, height=200, font=(None, text_size))
        self.console_log.grid(row=3, column=0, sticky="ew")
        self.console_log.bind("<Return>", self._submit_input)

        # Run button
        run_icon = PhotoImage(
            file = (
                "/home/olly/Documents/programming/other/rune_programming_language/code/"
                "IDE/run_icon.png"
            )
        )
        run_icon = run_icon.subsample(8, 8)
        self.run_button = ctk.CTkButton(
            self,
            image=run_icon,
            text="Run",
            command=self.run_command
        )
        self.run_button.grid(row=3, column=1)

    def open_file_command(self):
        """Runs the callback provided for the open file button click"""
        self.open_file_callback()

    def save_as_command(self):
        """Runs the callback provided for the save as button click"""
        self.save_as_callback()

    def save_command(self):
        """Runs the callback provided for the save button click"""
        self.save_callback()

    def run_command(self):
        """Runs the callback provided for the run button click"""
        self.run_callback()

    def register_open_file_callback(self, callback):
        """Registers the new callback for the open file button in the menu"""
        self.open_file_callback = callback

    def register_save_as_callback(self, callback):
        """Registers the new callback for the save as button in the menu"""
        self.save_as_callback = callback

    def register_save_callback(self, callback):
        """Registers the new callback for the save button in the menu"""
        self.save_callback = callback

    def register_run_callback(self, callback):
        """
        Registers the new callback for the run button in the menu, and the lower run
        button
        """
        self.run_callback = callback

    def get_code_window_text(self):
        """Returns the current text in the code window"""
        return self.text_box.get("1.0", "end")

    def set_code_window_text(self, new_text):
        """Sets the code window text"""
        self.text_box.delete("1.0", "end")
        self.text_box.insert("1.0", new_text)

    def request_save_path(self):
        """Produces a pop-up asking the user for a file path to save to"""
        return tkinter.filedialog.asksaveasfilename()

    def request_open_path(self):
        """Produces a pop-up asking the user for a file path to open"""
        return tkinter.filedialog.askopenfilename()

    def display_error_message(self, error_message):
        """Shows an error message pop-up"""
        MessageBox("Error", error_message)

    def append_to_console(self, text):
        """Appends given text to the console's text using the UI thread"""
        self.after(0, lambda: self._append_to_console_unsafe(text))

    def _append_to_console_unsafe(self, text):
        """
        Appends given text to the console's text - unsafe because this method assumes
        that it is being called on the UI thread
        """
        self.console_log.insert("end", text)
        self.console_log.see("end")

    def _submit_input(self, event):
        """Function to call when enter is pressed in console. Handles user input"""
        self.input_value = self.console_log.get("end-1c linestart", "end-1c lineend") # Last line of console
        self.input_event.set() # Sets the flag to true (thread shouldn't wait any longer)

    def get_input(self, prompt):
        """
        Function to replace the built-in input() function (so that IDE handles input
        rather than terminal)
        """
        self.input_event.clear() # Resets flag to false
        self.append_to_console(f"{prompt}\n")
        self.input_event.wait() # Thread waits in background, until flag is changed

        return self.input_value

    def clear_console(self):
        """Removes all current text from the console"""
        self.console_log.delete("1.0", "end")
