from tkinter import *
import tkinter.filedialog

class MenuBar(Menu):
    """The menu bar which runs along the top of the window"""

    def __init__(self, bg=None, activebackground=None, activeforeground=None):
        super().__init__(
            bg=bg,
            activebackground=activebackground,
            activeforeground=activeforeground
        )

        # Button callbacks
        self.open_file_callback = None

        # File menu
        file_menu = Menu(
            self,
            tearoff=0,
            bg=bg,
            activebackground=activebackground,
            activeforeground=activeforeground
        )
        self.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open file...", command=self.open_file_command)
        file_menu.add_command(label="Save", command=None)
        file_menu.add_command(label="Save as...", command=None)

        # Run menu
        run_menu = Menu(
            self,
            tearoff=0,
            bg=bg,
            activebackground=activebackground,
            activeforeground=activeforeground
        )
        self.add_cascade(label="Run", menu=run_menu)
        run_menu.add_command(label="Run current file", command=None)

    def open_file_command(self):
        """
        Runs the provided callback for the open file button
        """
        self.open_file_callback()

    def register_open_file_callback(self, callback):
        """
        Updates the callback for the open file button
        """
        self.open_file_callback = callback
