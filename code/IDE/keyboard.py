from tkinter import *
import math
import customtkinter as ctk

class KeyboardFrame(ctk.CTkFrame):
    """A customtkinter frame which displays the keyboard"""

    def __init__(self, master):
        super().__init__(master)

        key_chars = (
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3",
            "4", "5", "6", "7", "8", "9"
        )
        num_rows = 3
        num_cols = math.ceil(len(key_chars) / num_rows)

        for i, key_char in enumerate(key_chars):
            row = i // num_cols
            col = i % num_cols
            key_button = ctk.CTkButton(self, text=key_char)
            key_button.grid(row=row, column=col, sticky="ew")
