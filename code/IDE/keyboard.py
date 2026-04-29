from tkinter import *
import math
import customtkinter as ctk
from keyboard_key_data import KeyboardKeyData

class KeyboardFrame(ctk.CTkFrame):
    """A customtkinter frame which displays the keyboard"""

    def __init__(self, master, button_text_size=20, button_grid_padding=1):
        super().__init__(master)
        self.key_callback = None

        # Colour constants
        self.KEYWORD_COLOUR = "dark olive green"
        self.NATIVE_FUNCTION_COLOUR = "olive drab"
        self.BOOLEAN_COLOUR = "sea green"
        self.NUMBER_COLOUR = "medium sea green"

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
                fg_color=cur_key_data.colour,
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
            fg_color=self.KEYWORD_COLOUR,
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
            KeyboardKeyData("ᚢ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛒ", colour=self.KEYWORD_COLOUR), 
            KeyboardKeyData("ᛚ", colour=self.KEYWORD_COLOUR), 
            KeyboardKeyData("ᚫ", colour=self.KEYWORD_COLOUR), 
            KeyboardKeyData("ᚲ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᚿ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛆ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛅᚺᛣ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛒᛖᛏ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛖ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛢ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛖᛏ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛉᛖᛚ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛁᛩ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᚺᛅᛁᛩ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᚺᛅᛣ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛞ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛩᛟᛉᚴ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛧ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛧᛧ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᚺ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᚻ", colour=self.KEYWORD_COLOUR),
            KeyboardKeyData("ᛝ", colour=self.KEYWORD_COLOUR),
            # Native functions
            KeyboardKeyData("ᚹᛏᛁᛉᛚ", colour=self.NATIVE_FUNCTION_COLOUR),
            KeyboardKeyData("ᛉᛟᛒ", colour=self.NATIVE_FUNCTION_COLOUR),
            KeyboardKeyData("ᛁᛉᚹ", colour=self.NATIVE_FUNCTION_COLOUR), 
            KeyboardKeyData("ᛅᚺᛉ", colour=self.NATIVE_FUNCTION_COLOUR),
            # Boolean
            KeyboardKeyData("ᚸ", colour=self.BOOLEAN_COLOUR),
            KeyboardKeyData("ᚷ", colour=self.BOOLEAN_COLOUR),
            # Number related
            KeyboardKeyData("ᛄ", colour=self.NUMBER_COLOUR),
            KeyboardKeyData("ᛁ", colour=self.NUMBER_COLOUR),
            KeyboardKeyData(".", colour=self.NUMBER_COLOUR),
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
