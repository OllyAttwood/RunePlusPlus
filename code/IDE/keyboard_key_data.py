class KeyboardKeyData:
    """
    A class to store the data for a keyboard key - the string to be displayed, the key 
    colour, and the alternative text for a tooltip.
    """

    def __init__(self, text, colour=None, tooltip_text=None):
        self.text = text
        self.colour = colour
        self.tooltip_text = tooltip_text
