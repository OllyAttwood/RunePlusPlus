class TokenTypes:
    """The types of all tokens available"""

    # Numbers
    INT = "INT"
    FLOAT = "FLOAT"

    # Arithmetic operators
    ADD = "ADD"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"

    # Assignment
    ASSIGN = "ASSIGN"

    # Brackets
    LEFT_BRACKET = "LEFT_BRACKET"
    RIGHT_BRACKET = "RIGHT_BRACKET"

    # Groups of token types
    NUMBER_TYPES = (INT, FLOAT)
    UNARY_OPERATORS = (MINUS)
    EXPRESSION_OPERATORS = (ADD, MINUS)
    TERM_OPERATORS = (MULTIPLY, DIVIDE)
