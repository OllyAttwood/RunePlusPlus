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
        pre_tokens = self.pretokenise_str(self.text)

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

    def pretokenise_str(self, text, separator_char=SEPARATOR):
        """
        Splits the input text into 'pre-tokens' (before the more advanced tokenisation
        takes place) - a list of the text which has been split whenever there is a
        separator character. New line characters should also be their own element in the
        list.
        """
        cur_pretoken_text = ""
        pre_tokens = []
        new_line_char = "\n"

        for char in text:
            # If new pre-token should be added.
            # Also allows strings to contain otherwise functional characters such as '⋅'
            if (
                (char == separator_char or char == new_line_char)
                and not self.inside_string(cur_pretoken_text)
            ):
                # Don't add an empty string (consecutive new lines will result in this)
                if cur_pretoken_text != "":
                    pre_tokens.append(cur_pretoken_text)

                cur_pretoken_text = ""

                if char == new_line_char:
                    pre_tokens.append(char)
            else:
                cur_pretoken_text += char

        # Add the remaining pre-token
        if cur_pretoken_text != "":
            pre_tokens.append(cur_pretoken_text)

        return pre_tokens

    def inside_string(self, cur_pretoken_text):
        # If string so far is just an opening string symbol and nothing else
        if cur_pretoken_text == self.STRING_SYMBOL:
            return True

        # If string has been opened but not closed yet
        if (
            cur_pretoken_text.startswith(self.STRING_SYMBOL)
            and not cur_pretoken_text.endswith(self.STRING_SYMBOL)
        ):
            return True
        else:
            return False
