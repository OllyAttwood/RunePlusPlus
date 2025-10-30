from tkinter import *
#from tkinter.ttk import *
import math

class KeyboardFrame(Frame):
    """A tkinter frame which displays the keyboard"""

    def __init__(self, button_text_size=30):
        super().__init__()

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
            key_button = Button(self, text=key_char, font=(None, button_text_size))
            key_button.grid(row=row, column=col, sticky="ew")
