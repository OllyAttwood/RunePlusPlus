from token_types import TokenTypes as TT
from token_ import Token
from token_map import TOKEN_TYPE_DICT

class Lexer:
    """
    Splits the input into tokens which are ready for parsing, e.g. INT, STR, BOOLEAN etc
    """

    SEPARATOR = "⋅"
    DIGITS = "ᛄᛁ"
    DECIMAL_POINT = "."
    MINUS = "ᛒ"

    def __init__(self, text):
        self.text = text
        self.tokens = None

    def lex(self):
        """Splits the text into tokens for parsing"""
        self.tokens = []
        lines = self.text.split("\n")

        for line in lines:
            token_line = []
            # Tokens before more advanced processing
            pre_tokenised_line = line.split("⋅")

            # Determine full tokens
            for pre_token in pre_tokenised_line:
                token = self.get_token(pre_token)
                token_line.append(token)

            self.tokens.append(token_line)

    def get_token(self, text):
        """Computes the token from the provided text"""
        try:
            token_type = TOKEN_TYPE_DICT[text]

            return Token(token_type)
        except KeyError:
            number_type = self.is_a_number(text) # None, if text is not a number
            if number_type:
                return Token(number_type, text)

    def is_a_number(self, text):
        """
        Returns the token type (int or float) if the text is a number, otherwise returns
        None
        """
        # Handles negative numbers
        if text[0] == self.MINUS:
            text = text[1:]

        if set(text) <= set(self.DIGITS + self.DECIMAL_POINT):
            num_decimal_points = text.count(self.DECIMAL_POINT)
            if num_decimal_points == 0:
                return TT.INT
            elif num_decimal_points == 1:
                return TT.FLOAT

        return None
