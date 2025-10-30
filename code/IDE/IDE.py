"""Script to run an IDE to edit and run .RUNE files"""

from tkinter import *
#from tkinter.ttk import *
import menu_bar
import keyboard

# Window setup
root = Tk()
root.title("Rune++ IDE")
root.attributes("-zoomed", True) # Full-screen
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
text_size = 15

# Menu bar
menu = menu_bar.MenuBar()
root.config(menu=menu)

# Text box
text_box = Text(root, font=(None, text_size))
text_box.grid(row=0, column=0, columnspan=2, sticky="nesw")

# Keyboard
keyboard = keyboard.KeyboardFrame()
keyboard.grid(row=1, column=0, columnspan=2)

# Output log
output_log = Text(root, height=10, font=(None, text_size))
output_log.configure(state="disabled")
output_log.grid(row=2, column=0, sticky="ew")

# Run button
run_icon = PhotoImage(file="/home/olly/Documents/programming/other/rune_programming_language/code/IDE/run_icon.png")
run_icon = run_icon.subsample(8, 8)
run_button = Button(root, image=run_icon)
run_button.grid(row=2, column=1)

root.mainloop()
