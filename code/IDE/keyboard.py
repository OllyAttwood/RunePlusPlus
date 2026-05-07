import tkinter as tk
import math
import customtkinter as ctk
from keyboard_key_data import KeyboardKeyData

class KeyboardFrame(ctk.CTkFrame):
    """A customtkinter frame which displays the keyboard"""

    BUTTON_TEXT_SIZE = 20
    BUTTON_GRID_PADDING = 1
    # How far the tooltip should be from the cursor
    TOOLTIP_OFFSET = 10
    TOOLTIP_FONT_SIZE = 17
    TOOLTIP_PADDING = 20

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.key_callback = None
        self.tooltip = None

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
        Creates a key button, attaches the tooltip bindings, and adds it to the grid.
        """
        key_button = ctk.CTkButton(
            self,
            text=key_data.text,
            font=(None, self.BUTTON_TEXT_SIZE),
            fg_color=key_data.colour,
            command=lambda char=key_data.text: self.key_callback(char)
        )
        self.setup_button_tooltip_bindings(key_button, key_data.tooltip_text)
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

    def setup_button_tooltip_bindings(self, button, tooltip_text):
        """Adds the enter/leave bindings for a keyboard button to handle the tooltip."""
        button.bind(
            "<Enter>",
            lambda event: self.on_mouse_enter_button(event, tooltip_text)
        )
        button.bind("<Motion>", self.on_mouse_motion)
        button.bind("<Leave>", self.on_mouse_leave_button)

    def on_mouse_enter_button(self, event, tooltip_text):
        """
        Sets up the new tooltip if any previous tooltip has been destroyed, and there is
        some tooltip_text provided
        """
        if not self.tooltip and tooltip_text:
            self.tooltip = ctk.CTkLabel(
                self.master, 
                text=tooltip_text, 
                font=(None, self.TOOLTIP_FONT_SIZE),
                padx=self.TOOLTIP_PADDING
            )

    def on_mouse_motion(self, event):
        """Moves the tooltip with the user cursor"""
        if self.tooltip:
            # Co-ordinates are calculated relative to the keyboard frame and entire 
            # window
            x = (
                    event.widget.winfo_rootx() + event.x - self.master.winfo_x()
                     + self.TOOLTIP_OFFSET
            )
            y = (
                    event.widget.winfo_rooty() + event.y - self.master.winfo_y()
                     + self.TOOLTIP_OFFSET
            )
            
            self.tooltip.place(x=x, y=y)

    def on_mouse_leave_button(self, event):
        """
        Destroys the current tooltip, ready to setup a new one. The text on the button 
        is actually implemented as a Label, therefore we need to account for this 
        by checking the cursor has truly left the entire button and not just the label.
        """
        if self.tooltip and not isinstance(event.widget, tk.    Label):
            # Check cursor has actually left the button, rather than just being over 
            # the text label within the button
            button = event.widget
            # Cursor location
            absolute_x = event.x_root
            absolute_y = event.y_root

            # Button bounds
            x_lower_limit = button.winfo_rootx()
            y_lower_limit = button.winfo_rooty()
            x_upper_limit = x_lower_limit + button.winfo_width()
            y_upper_limit = y_lower_limit + button.winfo_height()

            if (
                absolute_x < x_lower_limit or absolute_x >= x_upper_limit
                or absolute_y < y_lower_limit or absolute_y >= y_upper_limit
            ):
                self.tooltip.destroy()
                self.tooltip = None
