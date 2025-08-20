class RunePlusPlusError(Exception):
    """Error class for when there is a mistake in the user's code"""

    DEFAULT_TEXT = "Rune++ Error!"

    def __init__(self, error_text=DEFAULT_TEXT):
        self.error_text = error_text
        super().__init__(error_text)
