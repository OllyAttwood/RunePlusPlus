"""
Tests for the lexer.py functions.

If the command "pytest" doesn't work (as it didn't for me), use
"python -m pytest" instead.

Run the command from the code/rune++ directory.

See https://www.tutorialspoint.com/pytest/index.htm for more help
"""

import pytest
from token_types import TokenTypes as TT
from lexer import Lexer

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("ᛁᛄᛁᛄ", TT.INT),
        ("ᛄ", TT.INT),
        ("ᛁ", TT.INT),
        ("ᛄᛄᛄ", TT.INT),
        ("ᛁᛁᛁ", TT.INT),
        ("ᛁᛄ.ᛁᛄ", TT.FLOAT),
        ("ᛄ.ᛄᛁ", TT.FLOAT),
        (".ᛁᛄ", TT.FLOAT),
        ("ᛁᛄ.", TT.FLOAT),
        ("", None),
        ("10", None),
        ("ᛁᛄ.ᛁᛄ.ᛁᛄ", None),
    ]
)
def test_is_a_number(input_text, expected_output):
    """
    Tests the is_a_number() function by comparing the result with the expected output
    """
    lexer = Lexer("")
    output = lexer.is_a_number(input_text)

    assert output == expected_output

def test_get_token():
    pass

def test_lex():
    pass
