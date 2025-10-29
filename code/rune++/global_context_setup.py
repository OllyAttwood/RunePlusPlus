"""Module for setting up the global variables"""
from context import Context, SymbolTable

def init_global_context():
    global_context = Context("global_context", symbol_table=SymbolTable())
    # True and False variables
    global_context.symbol_table.set("ᚷ", False)
    global_context.symbol_table.set("ᚸ", True)

    return global_context
