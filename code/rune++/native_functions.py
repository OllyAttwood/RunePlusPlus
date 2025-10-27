"""Functions provided by the programming language to provide core functionality"""
from inspect import getmembers, isfunction
import sys
from output_formatter import OutputFormatter
import token_map
from errors import RunePlusPlusError
import number_converter
from lexer import Lexer

def ᚹᛏᛁᛉᛚ(to_print):
    """The print function"""
    formatted = OutputFormatter(to_print).format()
    print(formatted)

def ᛉᛟᛒ(runes_str):
    """Converts a string to an int/float (whichever one applies)"""
    # Validate string
    digit_chars = number_converter.DIGIT_MAP["0"] + number_converter.DIGIT_MAP["1"]
    decimal_point = set(runes_str) - set(digit_chars)
    decimal_point = "".join(decimal_point) # Convert set to string

    if (
        not(decimal_point == "." or decimal_point == "")
        or runes_str.count(Lexer.DECIMAL_POINT) > 1
    ):
        raise RunePlusPlusError(
            "String contains characters which can't be converted to an int/float!"
        )

    # Convert string
    number = number_converter.from_runes_to_base10(runes_str)

    return number

def ᛁᛉᚹ(input_prompt=""):
    """The input (string) function"""
    input_str = input(input_prompt)

    # Validate input
    if any([char not in token_map.VARIABLE_NAME_CHARS for char in input_str]):
        raise RunePlusPlusError("Invalid characters entered!")

    return input_str

def ᛅᚺᛉ(list_):
    """Returns the length of a list (the len() function)"""
    if not isinstance(list_, list):
        raise RunePlusPlusError("Error calling ᛅᚺᛉ function: list not given")

    return len(list_)

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
