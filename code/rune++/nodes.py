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

    def __init__(self, operator_token, left_node_token, right_node_token):
        self.operator_token = operator_token
        self.left_node_token = left_node_token
        self.right_node_token = right_node_token

    def __repr__(self):
        return (
            f"<BinaryOperationNode: {self.left_node_token}, {self.operator_token}, "
            f"{self.right_node_token}>"
        )
