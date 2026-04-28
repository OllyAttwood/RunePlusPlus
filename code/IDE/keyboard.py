from tkinter import *
import math
import customtkinter as ctk

class KeyboardFrame(ctk.CTkFrame):
    """A customtkinter frame which displays the keyboard"""

    def __init__(self, master, button_text_size=20, button_grid_padding=1):
        super().__init__(master)
        self.key_callback = None

        # All chars except separator, which will be added separately
        key_chars = (
            # From token_map.py
            "ᚢ", "ᛒ", "ᛚ", "ᚫ", "ᚲ", "ᚿ", "ᛆ", "ᛅᚺᛣ", "ᛒᛖᛏ", "ᛖ", "ᛢ", "ᛖᛏ", "ᛉᛖᛚ",
            "ᛁᛩ", "ᚺᛅᛁᛩ", "ᚺᛅᛣ", "ᛞ", "ᛩᛟᛉᚴ", "ᛧ", "ᛧᛧ", "ᚺ", "ᚻ", "ᛝ",
            # Native functions
            "ᚹᛏᛁᛉᛚ", "ᛉᛟᛒ", "ᛁᛉᚹ", "ᛅᚺᛉ",
            # Boolean
            "ᚸ", "ᚷ",
            # Number related
            "ᛄ", "ᛁ", ".",
            # Remaining variable name characters
            "ᚹ", "ᚱ", "ᛩ", "ᛐ", "ᛏ", "ᚳ", "ᛣ", "ᚴ", "ᚠ", "ᛉ", "ᚩ", "ᛠ", "ᛈ", "ᛕ", "ᛅ",
            "ᚾ", "ᛡ", "ᛋ", "ᛟ"
        )
        separator_char = "⋅"
        num_rows = 6
        num_cols = math.ceil(len(key_chars) / num_rows)

        # Add regular key buttons
        for i, key_char in enumerate(key_chars):
            row = i // num_cols
            col = i % num_cols
            key_button = ctk.CTkButton(
                self,
                text=key_char,
                font=(None, button_text_size),
                command=lambda char=key_char: self.key_callback(char)
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
