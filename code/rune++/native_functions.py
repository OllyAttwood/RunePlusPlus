"""Functions provided by the programming language to provide core functionality"""
from inspect import getmembers, isfunction
import sys

def ᚹᛏᛁᛉᛚ(x):
    "The print function"
    print(x)

def get_function_from_name(function_name):
    """
    Returns the actual function from the name if it exists in this module, otherwise
    return None
    """
    current_module = sys.modules[__name__]
    module_function_tuples = getmembers(current_module, isfunction)

    for name, function in module_function_tuples:
        if function_name == name:
            return function

    return None
