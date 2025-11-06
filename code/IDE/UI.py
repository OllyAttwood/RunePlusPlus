import customtkinter as ctk
from tkinter import *
import tkinter.filedialog
import menu_bar
import keyboard

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
        self.console_log.configure(state="disabled")
        self.console_log.grid(row=3, column=0, sticky="ew")

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
