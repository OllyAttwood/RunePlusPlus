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
        "ᛆ": TT.RIGHT_BRACKET,
        "ᛅᚺᛣ": TT.LESS_THAN,
        "ᛒᛖᛏ": TT.MORE_THAN,
        "ᛖ": TT.EQUALS,
        "ᛢ": TT.AND,
        "ᛖᛏ": TT.OR,
        "ᛉᛖᛚ": TT.NOT,
        "ᛁᛩ": TT.IF,
        "ᚺᛅᛁᛩ": TT.ELIF,
        "ᚺᛅᛣ": TT.ELSE,
        "⋮": TT.CONTROL_FLOW_TERMINATOR,
        "ᛞ": TT.WHILE,
        "ᛩᛟᛉᚴ": TT.FUNCTION_DEFINITION,
        "ᛧ": TT.COMMA,
        "ᛧᛧ": TT.STRING,
        "ᚺ": TT.LEFT_SQUARE_BRACKET,
        "ᚻ": TT.RIGHT_SQUARE_BRACKET,
        "ᛝ": TT.LIST_INDEXER,
        "\n": TT.NEW_LINE
    }

def create_reverse_token_type_dict(original_dict):
    """
    Creates a reversed version of the dictionary so that the original keys can be
    accessed from their values
    """

    return {value: key for key, value in original_dict.items()}

TOKEN_TYPE_DICT = create_token_type_dict()
REVERSE_TOKEN_TYPE_DICT = create_reverse_token_type_dict(TOKEN_TYPE_DICT)
# All the characters that can be used in a variable name
VARIABLE_NAME_CHARS = "ᚹᚱᛩᛄᛒᛚᚫᛐᛏᚳᛣᚴᚠᛉᚩᛠᛈᛕᛅᚾᛡᚲᚷᚸᛞᛁᛋᛟᛝᚺᚻᚢᛖᚿᛆᛧᛢ"
