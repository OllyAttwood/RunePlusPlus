import tkinter as tk
import math
import customtkinter as ctk
from keyboard_key_data import KeyboardKeyData
from tooltip import Tooltip

class KeyboardFrame(ctk.CTkFrame):
    """A customtkinter frame which displays the keyboard"""

    BUTTON_TEXT_SIZE = 20
    BUTTON_GRID_PADDING = 1

    def __init__(self, master):
        super().__init__(master)
        self.master = master
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
            self.create_and_grid_key_button(cur_key_data, row, col)

        # Add separator button
        separator_button_data = KeyboardKeyData(
            separator_char,
            self.KEYWORD_COLOUR,
            "Separator"
        )
        self.create_and_grid_key_button(
            separator_button_data, 
            row=num_rows, 
            col=3, 
            columnspan=3
        )

    def register_key_callback(self, callback):
        """Registers the new callback for the key press"""
        self.key_callback = callback

    def create_and_grid_key_button(self, key_data, row, col, columnspan=1):
        """
        Creates a key button, adds tooltip, and adds it to the grid.
        """
        key_button = ctk.CTkButton(
            self,
            text=key_data.text,
            font=(None, self.BUTTON_TEXT_SIZE),
            fg_color=key_data.colour,
            command=lambda char=key_data.text: self.key_callback(char)
        )
        
        # Creates tooltip if needed
        if key_data.tooltip_text:
            Tooltip(key_button, key_data.tooltip_text, self.master)

        key_button.grid(
            row=row,
            column=col,
            columnspan=columnspan,
            sticky="ew",
            padx=self.BUTTON_GRID_PADDING,
            pady=self.BUTTON_GRID_PADDING
        )

    def create_key_button_data(self):
        """Creates the data for the key buttons"""
        return (
            # From token_map.py
            KeyboardKeyData("ᚢ", self.KEYWORD_COLOUR, "+"),
            KeyboardKeyData("ᛒ", self.KEYWORD_COLOUR, "-"), 
            KeyboardKeyData("ᛚ", self.KEYWORD_COLOUR, "×"), 
            KeyboardKeyData("ᚫ", self.KEYWORD_COLOUR, "÷"), 
            KeyboardKeyData("ᚲ", self.KEYWORD_COLOUR, "="),
            KeyboardKeyData("ᚿ", self.KEYWORD_COLOUR, "("),
            KeyboardKeyData("ᛆ", self.KEYWORD_COLOUR, ")"),
            KeyboardKeyData("ᛅᚺᛣ", self.KEYWORD_COLOUR, "<"),
            KeyboardKeyData("ᛒᛖᛏ", self.KEYWORD_COLOUR, ">"),
            KeyboardKeyData("ᛖ", self.KEYWORD_COLOUR, "=="),
            KeyboardKeyData("ᛢ", self.KEYWORD_COLOUR, "And"),
            KeyboardKeyData("ᛖᛏ", self.KEYWORD_COLOUR, "Or"),
            KeyboardKeyData("ᛉᛖᛚ", self.KEYWORD_COLOUR, "Not"),
            KeyboardKeyData("ᛁᛩ", self.KEYWORD_COLOUR, "If"),
            KeyboardKeyData("ᚺᛅᛁᛩ", self.KEYWORD_COLOUR, "Elif"),
            KeyboardKeyData("ᚺᛅᛣ", self.KEYWORD_COLOUR, "Else"),
            KeyboardKeyData("ᛞ", self.KEYWORD_COLOUR, "While"),
            KeyboardKeyData("ᛩᛟᛉᚴ", self.KEYWORD_COLOUR, "Function Declaration"),
            KeyboardKeyData("ᛧ", self.KEYWORD_COLOUR, ","),
            KeyboardKeyData("ᛧᛧ", self.KEYWORD_COLOUR, "\""),
            KeyboardKeyData("ᚺ", self.KEYWORD_COLOUR, "["),
            KeyboardKeyData("ᚻ", self.KEYWORD_COLOUR, "]"),
            KeyboardKeyData("ᛝ", self.KEYWORD_COLOUR, "List Indexer"),
            # Native functions
            KeyboardKeyData("ᚹᛏᛁᛉᛚ", self.NATIVE_FUNCTION_COLOUR, "Print"),
            KeyboardKeyData("ᛉᛟᛒ", self.NATIVE_FUNCTION_COLOUR, "Str_to_num"),
            KeyboardKeyData("ᛁᛉᚹ", self.NATIVE_FUNCTION_COLOUR, "Input"), 
            KeyboardKeyData("ᛅᚺᛉ", self.NATIVE_FUNCTION_COLOUR, "Length"),
            # Boolean
            KeyboardKeyData("ᚸ", self.BOOLEAN_COLOUR, "True"),
            KeyboardKeyData("ᚷ", self.BOOLEAN_COLOUR, "False"),
            # Number related
            KeyboardKeyData("ᛄ", self.NUMBER_COLOUR, "0"),
            KeyboardKeyData("ᛁ", self.NUMBER_COLOUR, "1"),
            KeyboardKeyData(".", self.NUMBER_COLOUR, "."),
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
