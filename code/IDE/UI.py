import customtkinter as ctk
from tkinter import *
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

        # Menu bar
        menu = menu_bar.MenuBar(
            bg="grey",
            activebackground="#36454F"
        )
        self.config(menu=menu)

        # Text box
        text_box = ctk.CTkTextbox(self, font=(None, text_size))
        text_box.grid(row=0, column=0, columnspan=2, sticky="nesw")

        # Keyboard
        keyboard_frame = keyboard.KeyboardFrame(self)
        keyboard_frame.grid(row=1, column=0, columnspan=2)

        # Console log
        console_log_label = ctk.CTkLabel(self, text="Console")
        console_log_label.grid(row=2, column=0, sticky="w")
        console_log = ctk.CTkTextbox(self, height=200, font=(None, text_size))
        console_log.configure(state="disabled")
        console_log.grid(row=3, column=0, sticky="ew")

        # Run button
        run_icon = PhotoImage(
            file = (
                "/home/olly/Documents/programming/other/rune_programming_language/code/"
                "IDE/run_icon.png"
            )
        )
        run_icon = run_icon.subsample(8, 8)
        run_button = ctk.CTkButton(self, image=run_icon, text="Run")
        run_button.grid(row=3, column=1)

        self.mainloop()
