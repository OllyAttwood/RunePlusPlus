from tkinter import *
import math
import customtkinter as ctk
from keyboard_key_data import KeyboardKeyData

class KeyboardFrame(ctk.CTkFrame):
    """A customtkinter frame which displays the keyboard"""

    def __init__(self, master, button_text_size=20, button_grid_padding=1):
        super().__init__(master)
        self.key_callback = None

        # All chars except separator, which will be added separately
        key_button_data = self.create_key_button_data()
        separator_char = "⋅"
        num_rows = 6
        num_cols = math.ceil(len(key_button_data) / num_rows)

        # Add regular key buttons
        for i, cur_key_data in enumerate(key_button_data):
            row = i // num_cols
            col = i % num_cols
            key_button = ctk.CTkButton(
                self,
                text=cur_key_data.text,
                font=(None, button_text_size),
                command=lambda char=cur_key_data.text: self.key_callback(char)
            )
            key_button.grid(
                row=row,
                column=col,
                sticky="ew",
                padx=button_grid_padding,
                pady=button_grid_padding
            )

        # Add separator button
        separator_button = ctk.CTkButton(
            self,
            text=separator_char,
            font=(None, button_text_size),
            command=lambda char=separator_char: self.key_callback(char)
        )
        separator_button.grid(
            row=num_rows,
            column=3,
            sticky="ew",
            padx=button_grid_padding,
            pady=button_grid_padding,
            columnspan=3
        )

    def register_key_callback(self, callback):
        """Registers the new callback for the key press"""
        self.key_callback = callback

    def create_key_button_data(self):
        """Creates the data for the key buttons"""
        return (
            # From token_map.py
            KeyboardKeyData("ᚢ"),
            KeyboardKeyData("ᛒ"), 
            KeyboardKeyData("ᛚ"), 
            KeyboardKeyData("ᚫ"), 
            KeyboardKeyData("ᚲ"),
            KeyboardKeyData("ᚿ"),
            KeyboardKeyData("ᛆ"),
            KeyboardKeyData("ᛅᚺᛣ"),
            KeyboardKeyData("ᛒᛖᛏ"),
            KeyboardKeyData("ᛖ"),
            KeyboardKeyData("ᛢ"),
            KeyboardKeyData("ᛖᛏ"),
            KeyboardKeyData("ᛉᛖᛚ"),
            KeyboardKeyData("ᛁᛩ"),
            KeyboardKeyData("ᚺᛅᛁᛩ"),
            KeyboardKeyData("ᚺᛅᛣ"),
            KeyboardKeyData("ᛞ"),
            KeyboardKeyData("ᛩᛟᛉᚴ"),
            KeyboardKeyData("ᛧ"),
            KeyboardKeyData("ᛧᛧ"),
            KeyboardKeyData("ᚺ"),
            KeyboardKeyData("ᚻ"),
            KeyboardKeyData("ᛝ"),
            # Native functions
            KeyboardKeyData("ᚹᛏᛁᛉᛚ"),
            KeyboardKeyData("ᛉᛟᛒ"),
            KeyboardKeyData("ᛁᛉᚹ"), 
            KeyboardKeyData("ᛅᚺᛉ"),
            # Boolean
            KeyboardKeyData("ᚸ"),
            KeyboardKeyData("ᚷ"),
            # Number related
            KeyboardKeyData("ᛄ"),
            KeyboardKeyData("ᛁ"),
            KeyboardKeyData("."),
            # Remaining variable name characters
            KeyboardKeyData("ᚹ"),
            KeyboardKeyData("ᚱ"),
            KeyboardKeyData("ᛩ"), 
            KeyboardKeyData("ᛐ"),
            KeyboardKeyData("ᛏ"),
            KeyboardKeyData("ᚳ"), 
            KeyboardKeyData("ᛣ"),
            KeyboardKeyData("ᚴ"),
            KeyboardKeyData("ᚠ"), 
            KeyboardKeyData("ᛉ"),
            KeyboardKeyData("ᚩ"),
            KeyboardKeyData("ᛠ"), 
            KeyboardKeyData("ᛈ"),
            KeyboardKeyData("ᛕ"),
            KeyboardKeyData("ᛅ"),
            KeyboardKeyData("ᚾ"),
            KeyboardKeyData("ᛡ"),
            KeyboardKeyData("ᛋ"), 
            KeyboardKeyData("ᛟ")
        )
