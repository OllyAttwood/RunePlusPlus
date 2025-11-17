from customtkinter import *

class MessageBox(CTkToplevel):
    """A basic pop-up window"""

    def __init__(self, title, message):
        super().__init__()
        self.title(title)
        self.geometry("300x150")
        # lock popup at front
        self.attributes("-topmost", "true")
        # make main window unclickable until popup is closed
        self.lock_at_front()
        #keep widgets in centre during resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #widgets
        message_label = CTkLabel(self, text=message, wraplength=250)
        message_label.grid(row=0, column=0)

        ok_button = CTkButton(
            self, text="OK", command=self.release_focus_and_hide
        )
        ok_button.grid(row=1, column=0)

    def release_focus_and_hide(self):
        """Hides the window"""
        self.grab_release()
        self.withdraw()

    def lock_at_front(self):
        """Makes main window unclickable until popup is closed"""
        self.wait_visibility() # https://raspberrypi.stackexchange.com/a/105522
        self.grab_set()
