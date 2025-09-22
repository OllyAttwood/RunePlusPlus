"""The nodes used in an Abstract Syntax Tree"""

class NumberNode:
    """A node which contains only a number (integer or float)"""

    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f"<NumberNode: {self.token}>"

class BinaryOperationNode:
    """
    A node which represents any sort of binary operation i.e. an operator which has two
    operands. For example '1 + 2' or '3 * (4 + 5)'
    """

    def __init__(self, operator_token, left_node, right_node):
        self.operator_token = operator_token
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self):
        return (
            f"<BinaryOperationNode: {self.left_node}, {self.operator_token}, "
            f"{self.right_node}>"
        )

class UnaryOperationNode:
    """
    A node which represents any sort of unary operation i.e. an operator which has one
    operand. For example '-1'.
    """

    def __init__(self, operator_token, operand_node):
        self.operator_token = operator_token
        self.operand_node = operand_node

    def __repr__(self):
        return f"<UnaryOperationNode: {self.operator_token}, {self.operand_node}>"

class VariableAssignmentNode:
    """A node which represents a variable being assigned a value"""

    def __init__(self, variable_name_token, value_node):
        self.variable_name_token = variable_name_token
        self.value_node = value_node

    def __repr__(self):
        return (
            f"<VariableAssignmentNode: {self.variable_name_token}, "
            f"{self.value_node}>"
        )

class VariableReadNode:
    """A node which represents a variable's value being read"""

    def __init__(self, variable_name_token):
        self.variable_name_token = variable_name_token

    def __repr__(self):
        return f"<VariableReadNode: {self.variable_name_token}>"

class IfStatementNode:
    """
    A node which represents an if statement (initial if as well as accompanying elifs
    and else)
    """

    def __init__(self, if_cases, else_case=None):
        self.if_cases = if_cases
        self.else_case = else_case

    def __repr__(self):
        else_str = "" if self.else_case is None else f", {self.else_case}"

        return f"<IfStatementNode: {self.if_cases}{else_str}>"

class WhileNode:
    """A node which represents a while loop"""

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"<WhileNode: {self.condition}, {self.body}>"
