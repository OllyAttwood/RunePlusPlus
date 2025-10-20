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

    def parse_all(self):
        """Attempts to parse all lines"""
        multi_line_node = self.parse_multi_lines()

        # self.cur_token should be None, otherwise it means something hasn't been parsed
        if self.cur_token != None:
            raise RunePlusPlusError(
                f"End of line not reached! Current token is {self.cur_token}"
            )

        return multi_line_node

    def parse_multi_lines(self, stop_at_blank_line=False):
        """
        Attempts to parse one or more expressions. If stop_at_blank_line is true, the
        parsing will stop when a blank line (two or more consecutive new lines) is
        encountered, otherwise blank lines will be ignored.
        """
        expressions = []
        # Parse first expression
        expressions.append(self.parse_expression())

        # Parse optional extra expressions (each on a new line)
        while self.cur_token != None and self.cur_token.token_type == TT.NEW_LINE:
            self.next_token()

            if (
                stop_at_blank_line
                and self.cur_token != None and self.cur_token.token_type == TT.NEW_LINE
            ):
                break

            # If in the middle of an if/elif/else statement, stop at next case
            if (
                self.cur_token != None
                and self.cur_token.token_type in (TT.ELIF, TT.ELSE)
            ):
                break

            expressions.append(self.parse_expression())

        return MultiLineNode(expressions)

    def parse_expression(self):
        """
        Attempts to parse the current token(s) as a boolean expression (AND or OR
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

        return self.parse_binary_operation(
            self.parse_comparison_expression,
            TT.AND_OR_OPERATORS
        )

    def parse_comparison_expression(self):
        """
        Attempts to parse the current token(s) as a comparison expression (EQUALS,
        LESS_THAN or MORE_THAN operation). Also handles the NOT token if present.
        """
        # If the NOT unary operator is present
        if self.cur_token.token_type == TT.NOT:
            not_token = self.cur_token
            self.next_token()
            return UnaryOperationNode(not_token, self.parse_comparison_expression())
        else:
            return self.parse_binary_operation(
                self.parse_arithmetic_expression,
                TT.COMPARISON_OPERATORS
            )

    def parse_arithmetic_expression(self):
        """
        Attempts to parse the current token(s) as an arithmetic expression (add or
        minus operation)
        """
        return self.parse_binary_operation(self.parse_term, TT.EXPRESSION_OPERATORS)

    def parse_term(self):
        """
        Attempts to parse the current token(s) as a term (multiply or divide operation)
        """
        return self.parse_binary_operation(self.parse_list_indexing_expression, TT.TERM_OPERATORS)

    def parse_list_indexing_expression(self):
        """Attempts to parse the current token(s) as a list indexing expression"""
        return self.parse_binary_operation(self.parse_factor, [TT.LIST_INDEXER])

    def parse_binary_operation(self, operand_function, operators):
        """
        Attempts to parse the current token(s) as a term or expression, depending on
        provided paramters.
        operand_function is the function to parse the tokens on each side of the
            operator.
        operators is the applicable operators for this binary operation (add/subtract or
            multiply/divide).
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

        # Strings
        elif self.cur_token.token_type == TT.STRING:
            str_node = StringNode(self.cur_token)
            self.next_token()

            return str_node

        # Brackets
        elif self.cur_token.token_type == TT.LEFT_BRACKET:
            self.next_token()
            expression = self.parse_expression()

            if self.cur_token.token_type != TT.RIGHT_BRACKET:
                raise RunePlusPlusError("No closing bracket!")

            self.next_token()

            return expression

        # Square brackets
        elif self.cur_token.token_type == TT.LEFT_SQUARE_BRACKET:
            return self.parse_list()

        # Unary operators (negative numbers etc)
        elif self.cur_token.token_type in TT.UNARY_OPERATORS:
            operator_token = self.cur_token
            self.next_token()
            operand = self.parse_factor()

            return UnaryOperationNode(operator_token, operand)

        # Function call
        elif (
            self.cur_token.token_type == TT.VARIABLE_NAME
            and self.peek_next_token() != None
            and self.peek_next_token().token_type == TT.LEFT_BRACKET
        ):
            return self.parse_function_call()

        # Variable being read
        elif self.cur_token.token_type == TT.VARIABLE_NAME:
            variable_read_node = VariableReadNode(self.cur_token)
            self.next_token()

            return variable_read_node

        # If statement
        elif self.cur_token.token_type == TT.IF:
            return self.parse_if_expression()

        # While loop
        elif self.cur_token.token_type == TT.WHILE:
            return self.parse_while_expression()

        # Function definition
        elif self.cur_token.token_type == TT.FUNCTION_DEFINITION:
            return self.parse_function_definition()

    def parse_if_expression(self):
        """
        Attempts to parse the current tokens as an if statement, including possible elif
        and else cases
        """
        if_cases = []
        else_case = None

        # Inital if case
        if_first_case = self.parse_single_if_case()
        if_cases.append(if_first_case)

        # Loops through all elif cases
        while self.cur_token.token_type == TT.ELIF:
            elif_case = self.parse_single_if_case()
            if_cases.append(elif_case)

        # Else case
        if self.cur_token is not None and self.cur_token.token_type != TT.NEW_LINE:
            if self.cur_token.token_type == TT.ELSE:
                else_case = self.parse_single_else_case()
            else:
                raise RunePlusPlusError("Else case or blank line expected!")

        return IfStatementNode(if_cases, else_case)

    def parse_single_if_case(self):
        """
        Attempts to parse a single if/elif case (NOT to be used for else cases) and
        return the condition and body as a tuple
        """
        self.next_token() # Skips IF/ELIF token
        if_condition = self.parse_expression()

        if self.cur_token.token_type != TT.NEW_LINE:
            raise RunePlusPlusError(f"Expected new line, instead found {self.cur_token}")

        self.next_token()
        if_body = self.parse_multi_lines(stop_at_blank_line=True)

        return (if_condition, if_body)

    def parse_single_else_case(self):
        """
        Attempts to parse a single else case and return the body
        """
        self.next_token() # Skips ELSE token

        if self.cur_token.token_type != TT.NEW_LINE:
            raise RunePlusPlusError(f"Expected new line, instead found {self.cur_token}")

        self.next_token()
        else_body = self.parse_multi_lines(stop_at_blank_line=True)

        return else_body

    def parse_while_expression(self):
        """Attempts to parse a while loop"""
        self.next_token() # Skips WHILE token
        while_condition = self.parse_expression()

        if self.cur_token.token_type != TT.NEW_LINE:
            raise RunePlusPlusError(f"Expected new line, instead found {self.cur_token}")

        self.next_token()
        while_body = self.parse_multi_lines(stop_at_blank_line=True)

        return WhileNode(while_condition, while_body)

    def parse_function_definition(self):
        """
        Attempts to parse a function definition, including parameters which may or may
        not be included
        """
        parameter_name_tokens = []
        self.next_token() # Skip 'function' keyword
        function_variable_name_token = self.cur_token

        if function_variable_name_token.token_type != TT.VARIABLE_NAME:
            raise RunePlusPlusError("Function name not provided!")

        self.next_token()

        # Check for first parameter
        if self.cur_token.token_type == TT.VARIABLE_NAME:
            parameter_name_tokens.append(self.cur_token)
            self.next_token()

            # Check for extra function parameters
            while self.cur_token.token_type != TT.NEW_LINE:
                if self.cur_token.token_type != TT.COMMA:
                    raise RunePlusPlusError(
                        "Comma expected to separate function parameters!"
                    )

                self.next_token()

                if self.cur_token.token_type != TT.VARIABLE_NAME:
                    raise RunePlusPlusError("Parameter name expected!")

                parameter_name_tokens.append(self.cur_token)
                self.next_token()

        if self.cur_token.token_type != TT.NEW_LINE:
            raise RunePlusPlusError(f"Expected new line, instead found {self.cur_token}")

        self.next_token() # Skip NEW_LINE token
        body_node = self.parse_multi_lines(stop_at_blank_line=True)

        return FunctionDefinitionNode(
            function_variable_name_token,
            parameter_name_tokens,
            body_node
        )

    def parse_function_call(self):
        """Attempts to parse a function call"""
        function_variable_name_token = self.cur_token
        parameter_nodes = []
        self.next_token()

        if self.cur_token.token_type != TT.LEFT_BRACKET:
            raise RunePlusPlusError("Left bracket expected for a function call!")

        self.next_token()

        # If no parameters included
        if self.cur_token.token_type == TT.RIGHT_BRACKET:
            self.next_token()
        # If there are parameters
        else:
            parameter_nodes.append(self.parse_expression())

            while self.cur_token.token_type == TT.COMMA:
                self.next_token() # Skip comma
                new_parameter_node = self.parse_expression()
                parameter_nodes.append(new_parameter_node)

            if self.cur_token.token_type != TT.RIGHT_BRACKET:
                raise RunePlusPlusError(
                    "Expected a closing bracket with the function call!"
                )

            self.next_token()

        return FunctionCallNode(function_variable_name_token, parameter_nodes)

    def parse_list(self):
        element_nodes = []
        self.next_token() # Skip opening bracket

        if self.cur_token.token_type != TT.RIGHT_SQUARE_BRACKET:
            element_nodes.append(self.parse_expression()) # First element

            # All subsequent elements
            while (
                self.cur_token is not None
                and self.cur_token.token_type == TT.COMMA
            ):
                self.next_token()
                element_nodes.append(self.parse_expression())

            if (
                self.cur_token is None
                or self.cur_token.token_type != TT.RIGHT_SQUARE_BRACKET
            ):
                raise RunePlusPlusError("List parsing error!")

        self.next_token()
        return ListNode(element_nodes)
