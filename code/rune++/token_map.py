"""Stores the mapping of strings to token types"""

from token_types import TokenTypes as TT

def create_token_type_dict():
    """
    Sets up the dictionary which maps the token string representations to the token
    types e.g. "+" to TT.ADD
    """
    return {
        "ᚢ": TT.ADD,
        "ᛒ": TT.MINUS,
        "ᛚ": TT.MULTIPLY,
        "ᚫ": TT.DIVIDE,
        "ᚲ": TT.ASSIGN,
        "ᚿ": TT.LEFT_BRACKET,
        "ᛆ": TT.RIGHT_BRACKET
    }

TOKEN_TYPE_DICT = create_token_type_dict()
# All the characters that can be used in a variable name
VARIABLE_NAME_CHARS = "ᚹᚱᛩᛄᛒᛚᚫᛐᛏᚳᛣᚴᚠᛉᚩᛠᛈᛕᛅᚾᛡᚲᚷᚸᛞᛁᛋᛟᛝᚺᚻᚢᛖᚿᛆᛧᛢ"
