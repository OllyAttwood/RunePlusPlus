class Context:
    """
    Stores information about the current part (global, function, class etc) of the
    program, including its symbol table and parent context. This is needed to enforce
    different scopes.
    """

    def __init__(self, context_name, symbol_table=None, parent_context=None):
        self.context_name = context_name
        self.symbol_table = symbol_table
        self.parent_context = parent_context


class SymbolTable:
    """
    Stores information associated with identifiers (variables, functions, classes etc)
    """

    def __init__(self, parent_symbol_table=None):
        self.parent_symbol_table = parent_symbol_table
        self.symbols = {}

    def get(self, key):
        """
        Returns the value associated with the key from this symbol table. If not found,
        recursively searches the parent symbol tables for the key.
        """

        value = self.symbols.get(key)

        if value is None and self.parent_symbol_table is not None:
            return self.parent_symbol_table.get(key)
        else:
            return value

    def set(self, key, value):
        """Sets a value in the symbol table"""
        self.symbols[key] = value
