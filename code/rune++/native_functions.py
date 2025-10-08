"""Functions provided by the programming language to provide core functionality"""
from inspect import getmembers, isfunction
import sys
from output_formatter import OutputFormatter
import token_map
from errors import RunePlusPlusError

def ᚹᛏᛁᛉᛚ(to_print):
    """The print function"""
    formatted = OutputFormatter(to_print).format()
    print(formatted)

def ᛁᛉᚹ(input_prompt=""):
    """The input (string) function"""
    input_str = input(input_prompt)

    # Validate input
    if any([char not in token_map.VARIABLE_NAME_CHARS for char in input_str]):
        raise RunePlusPlusError("Invalid characters entered!")

    return input_str

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
