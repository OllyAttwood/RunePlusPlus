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

    # Variables
    VARIABLE_NAME = "VARIABLE_NAME"

    # Comparison operators
    LESS_THAN = "LESS_THAN"
    MORE_THAN = "MORE_THAN"
    EQUALS = "EQUALS" # This is NOT the assignment operator

    # Boolean operators
    AND = "AND"
    OR = "OR"
    NOT = "NOT"

    # Control flow
    IF = "IF"
    ELIF = "ELIF"
    ELSE = "ELSE"
    CONTROL_FLOW_TERMINATOR = "CONTROL_FLOW_TERMINATOR"
    WHILE = "WHILE"

    # Functions
    FUNCTION_DEFINITION = "FUNCTION_DEFINITION"

    # Other
    COMMA = "COMMA"

    # Groups of token types
    NUMBER_TYPES = (INT, FLOAT)
    UNARY_OPERATORS = (MINUS)
    EXPRESSION_OPERATORS = (ADD, MINUS)
    TERM_OPERATORS = (MULTIPLY, DIVIDE)
    COMPARISON_OPERATORS = (LESS_THAN, MORE_THAN, EQUALS)
    AND_OR_OPERATORS = (AND, OR) # Not including NOT
