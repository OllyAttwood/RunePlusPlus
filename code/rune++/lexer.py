from token_types import TokenTypes as TT
from token_ import Token
from token_map import TOKEN_TYPE_DICT, VARIABLE_NAME_CHARS
import number_converter
from errors import RunePlusPlusError

class Lexer:
    """
    Splits the input into tokens which are ready for parsing, e.g. INT, STR, BOOLEAN etc
    """

    SEPARATOR = "⋅"
    DIGITS = "ᛄᛁ"
    DECIMAL_POINT = "."
    STRING_SYMBOL = "ᛧᛧ"

    def __init__(self, text):
        self.text = text
        self.tokens = None

    def lex(self):
        """Splits the text into tokens for parsing"""
        self.tokens = []

        # Tokens before more advanced processing
        pre_tokens = self.text.split("⋅")

        # Determine full tokens
        for pre_token in pre_tokens:
            token = self.get_token(pre_token)
            self.tokens.append(token)

    def get_token(self, text):
        """Computes the token from the provided text"""
        try:
            token_type = TOKEN_TYPE_DICT[text]

            return Token(token_type)
        except KeyError:
            number_type = self.is_a_number(text) # None, if text is not a number
            if number_type:
                value = number_converter.from_runes_to_base10(text)
                return Token(number_type, value)
            # String check
            elif (
                len(text) >= len(self.STRING_SYMBOL) * 2
                and text.startswith(self.STRING_SYMBOL)
                and text.endswith(self.STRING_SYMBOL)
            ):
                text_without_str_symbols = text[
                    len(self.STRING_SYMBOL) : -len(self.STRING_SYMBOL)
                ]
                return Token(TT.STRING, text_without_str_symbols)
            # The identifier elif should always be the last if statement
            elif set(text) <= set(VARIABLE_NAME_CHARS) and text != "":
                return Token(TT.VARIABLE_NAME, text)
            else:
                raise RunePlusPlusError("Tokenising error!")

    def is_a_number(self, text):
        """
        Returns the token type (int or float) if the text is a number, otherwise returns
        None
        """

        if set(text) <= set(self.DIGITS + self.DECIMAL_POINT) and text != "":
            num_decimal_points = text.count(self.DECIMAL_POINT)
            if num_decimal_points == 0:
                return TT.INT
            elif num_decimal_points == 1:
                return TT.FLOAT

        return None
