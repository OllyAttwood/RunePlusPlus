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
from token_ import Token
from errors import RunePlusPlusError

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
        ("ᛁᛄ.ᛁᛄ.ᛁᛄ", None)
    ]
)
def test_is_a_number(input_text, expected_output):
    """
    Tests the is_a_number() function by comparing the result with the expected output
    """
    lexer = Lexer("")
    output = lexer.is_a_number(input_text)

    assert output == expected_output

@pytest.mark.parametrize(
    "input_text, expected_token_type, expected_value",
    [
        ("ᛁᛄᛁᛄ", TT.INT, 10),
        ("ᛁᛁᛄ.ᛁᛄᛁ", TT.FLOAT, 6.625),
        ("ᚢ", TT.ADD, None),
        ("ᛒ", TT.MINUS, None),
        ("ᛚ", TT.MULTIPLY, None),
        ("ᚫ", TT.DIVIDE, None),
        ("ᚲ", TT.ASSIGN, None),
        ("ᚿ", TT.LEFT_BRACKET, None),
        ("ᛆ", TT.RIGHT_BRACKET, None)
    ]
)
def test_get_token_with_valid_inputs(input_text, expected_token_type, expected_value):
    """
    Tests the get_token() function by comparing the result with the expected output
    """
    lexer = Lexer("")
    output_token = lexer.get_token(input_text)

    assert expected_token_type == output_token.token_type
    assert expected_value == output_token.value

@pytest.mark.parametrize(
    "input_text",
    [
        "",
        " ",
        "abcd",
        "1234",
        "ᛒᛁᛄᛁᛄ"
    ]
)
def test_get_token_with_invalid_inputs(input_text):
    """
    Tests the get_token() correctly produces errors for invalid inputs
    """
    lexer = Lexer("")

    with pytest.raises(RunePlusPlusError): # This makes the test fail if an error is not raised
        lexer.get_token(input_text)

def test_lex():
    pass
