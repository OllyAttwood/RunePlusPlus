from tkinter import *
#from tkinter.ttk import *

class MenuBar(Menu):
    """The menu bar which runs along the top of the window"""

    def __init__(self):
        super().__init__()

        # File menu
        file_menu = Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open file...", command=None)
        file_menu.add_command(label="Save", command=None)
        file_menu.add_command(label="Save as...", command=None)

        # Run menu
        run_menu = Menu(self, tearoff=0)
        self.add_cascade(label="Run", menu=run_menu)
        run_menu.add_command(label="Run current file", command=None)
