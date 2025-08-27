class Token:
    """
    Represents a token with a token type, and optionally a value. File is named
    token_.py with an underscore so it doesn't collide with the Python file token.py.
    """

    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        value_str = ": " + str(self.value) if self.value else ""

        return f"<{self.token_type}{value_str}>"
