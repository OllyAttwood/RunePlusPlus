"""Script to run an IDE to edit and run .RUNE files"""

from UI import UI
from IDE_functions import IDE_Functions
from presenter import Presenter

view = UI()
model = IDE_Functions()
presenter = Presenter(view, model)

# main loop of UI must be started after all callbacks have been registered by the
# presenter
view.mainloop()
