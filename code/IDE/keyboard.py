from tkinter import *
import math
import customtkinter as ctk

class KeyboardFrame(ctk.CTkFrame):
    """A customtkinter frame which displays the keyboard"""

    def __init__(self, master):
        super().__init__(master)

        key_chars = (
            # From token_map.py
            "ᚢ", "ᛒ", "ᛚ", "ᚫ", "ᚲ", "ᚿ", "ᛆ", "ᛅᚺᛣ", "ᛒᛖᛏ", "ᛖ", "ᛢ", "ᛖᛏ", "ᛉᛖᛚ",
            "ᛁᛩ", "ᚺᛅᛁᛩ", "ᚺᛅᛣ", "ᛞ", "ᛩᛟᛉᚴ", "ᛧ", "ᛧᛧ", "ᚺ", "ᚻ", "ᛝ",
            # Boolean
            "ᚸ", "ᚷ",
            # Number related
            "ᛄ", "ᛁ", ".",
            # Remaining variable name characters
            "ᚹ", "ᚱ", "ᛩ", "ᛐ", "ᛏ", "ᚳ", "ᛣ", "ᚴ", "ᚠ", "ᛉ", "ᚩ", "ᛠ", "ᛈ", "ᛕ", "ᛅ",
            "ᚾ", "ᛡ", "ᛋ", "ᛟ",
            # Separator
            "⋅"
        )
        num_rows = 6
        num_cols = math.ceil(len(key_chars) / num_rows)

        for i, key_char in enumerate(key_chars):
            row = i // num_cols
            col = i % num_cols
            key_button = ctk.CTkButton(self, text=key_char)
            key_button.grid(row=row, column=col, sticky="ew")
