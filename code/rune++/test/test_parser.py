"""
Tests for the parser.py functions.

If the command "pytest" doesn't work (as it didn't for me), use
"python -m pytest" instead.

Run the command from the code/rune++ directory.

See https://www.tutorialspoint.com/pytest/index.htm for more help
"""

import pytest
from lexer import Lexer
from parser import Parser

@pytest.mark.parametrize(
    "runes_line, expected_ast_str_repr",
    [
        (
            "ᛁᛄ.ᛁᛄ⋅ᛚ⋅ᚿ⋅ᛁᛄᛁ⋅ᛚ⋅ᛁᛄᛁ⋅ᚢ⋅ᛒ⋅ᛁᛄᛁ⋅ᛆ",
            (
                "<BinaryOperationNode: <NumberNode: <FLOAT: 2.5>>, <MULTIPLY>, "
                "<BinaryOperationNode: <BinaryOperationNode: <NumberNode: <INT: 5>>, "
                "<MULTIPLY>, <NumberNode: <INT: 5>>>, <ADD>, <UnaryOperationNode: "
                "<MINUS>, <NumberNode: <INT: 5>>>>>"
            )
        ),
        (
            "ᛁᛁᛁᛄ⋅ᛒ⋅ᛁ.ᛄᛁ⋅ᚫ⋅ᛁᛄ",
            (
                "<BinaryOperationNode: <NumberNode: <INT: 14>>, <MINUS>, "
                "<BinaryOperationNode: <NumberNode: <FLOAT: 1.25>>, <DIVIDE>, "
                "<NumberNode: <INT: 2>>>>"
            )
        )
    ]
)
def test_parse_line(runes_line, expected_ast_str_repr):
    """
    Tests the parse_line() function by comparing the resulting abstract syntax tree's
    string representation with the expected output
    """
    lexer = Lexer(runes_line)
    lexer.lex()

    parser = Parser(lexer.tokens)
    ast = parser.parse_line()

    assert ast.__repr__() == expected_ast_str_repr
