from token_types import TokenTypes as TT
from nodes import *
from errors import RunePlusPlusError

class Parser:
    """
    Converts a list of tokens into an Abstract Syntax Tree (AST) representation of the
    program
    """

    def __init__(self, tokens):
        """
        The tokens parameter is a 2D list of tokens, where each row represents a row
        from the source code
        """
        self.tokens = tokens
        self.cur_index = 0
        self.cur_token = self.tokens[0]

    def next_token(self):
        """Moves to the next token"""
        self.cur_index += 1

        if self.cur_index >= len(self.tokens):
            self.cur_token = None
        else:
            self.cur_token = self.tokens[self.cur_index]

    def parse_line(self):
        """Calls parse_expression() but checks that the whole line has been parsed"""
        expression = self.parse_expression()

        # self.cur_token should be None, otherwise it means something hasn't been parsed
        if self.cur_token != None:
            raise RunePlusPlusError(
                f"End of line not reached! Current token is {self.cur_token}"
            )

        return expression

    def parse_expression(self):
        """
        Attempts to parse the current token(s) as an expression (add or subtract
        operation)
        """
        return self.parse_binary_operation(self.parse_term, [TT.ADD, TT.MINUS])

    def parse_term(self):
        """
        Attempts to parse the current token(s) as a term (multiply or divide operation)
        """
        return self.parse_binary_operation(self.parse_factor, [TT.MULTIPLY, TT.DIVIDE])

    def parse_binary_operation(self, operand_function, operators):
        """
        Attempts to parse the current token(s) as a term or expression, depending on
        provided paramters.
        operand_function is the function to parse the tokens on each side of the
            operator.
        operators is the applicable operators for this binary operation (add/subtract or
            mmultiply/divide).
        """
        left_node = operand_function()

        while (
            self.cur_token != None and
            self.cur_token.token_type in operators
        ):
            operator_token = self.cur_token
            self.next_token()
            right_node = operand_function()

            # Update left_node with the entire binary operation, including the previous
            # left_node
            left_node = BinaryOperationNode(operator_token, left_node, right_node)

        return left_node

    def parse_factor(self):
        """Attempts to parse the current token as a factor (number, identifier etc)"""
        # Numbers
        if self.cur_token.token_type in TT.NUMBER_TYPES:
            num_node = NumberNode(self.cur_token)
            self.next_token()

            return num_node

        # Brackets
        elif self.cur_token.token_type == TT.LEFT_BRACKET:
            self.next_token()
            expression = self.parse_expression()

            if self.cur_token.token_type != TT.RIGHT_BRACKET:
                print("--- Throw error here - no closing bracket ---")

            self.next_token()

            return expression

        # Unary operators (negative numbers etc)
        elif self.cur_token.token_type in TT.UNARY_OPERATORS:
            operand_token = self.cur_token
            self.next_token()
            operand = self.parse_factor()

            return UnaryOperationNode(operand_token, operand)
