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

    def peek_next_token(self):
        """
        Returns the next token without updating self.cur_index and self.cur_token.
        Returns None if there is no next token.
        """
        if self.cur_index + 1 >= len(self.tokens):
            return None
        else:
            return self.tokens[self.cur_index + 1]

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
        # If there is a variable assignment, prioritise it. This is so 'a = 1 + 2' is
        # treated as 'a = (1 + 2)' and not '(a = 1) + 2'
        if (
            self.cur_token.token_type == TT.VARIABLE_NAME
            and self.peek_next_token() is not None
            and self.peek_next_token().token_type == TT.ASSIGN
        ):
            var_name_token = self.cur_token
            self.next_token()
            self.next_token() # Skips the assignment token
            expression = self.parse_expression()

            return VariableAssignmentNode(
                var_name_token,
                expression
            )

        return self.parse_binary_operation(self.parse_term, TT.EXPRESSION_OPERATORS)

    def parse_term(self):
        """
        Attempts to parse the current token(s) as a term (multiply or divide operation)
        """
        return self.parse_binary_operation(self.parse_factor, TT.TERM_OPERATORS)

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
                raise RunePlusPlusError("No closing bracket!")

            self.next_token()

            return expression

        # Unary operators (negative numbers etc)
        elif self.cur_token.token_type in TT.UNARY_OPERATORS:
            operand_token = self.cur_token
            self.next_token()
            operand = self.parse_factor()

            return UnaryOperationNode(operand_token, operand)

        # Variable being read
        elif self.cur_token.token_type == TT.VARIABLE_NAME:
            variable_read_node = VariableReadNode(self.cur_token)
            self.next_token()

            return variable_read_node
