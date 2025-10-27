"""
Tests various use cases by using the entire programming language pipeline (i.e. similar
to how it's performed in temp.py).

If the command "pytest" doesn't work (as it didn't for me), use
"python -m pytest" instead.

Run the command from the code/rune++ directory.

See https://www.tutorialspoint.com/pytest/index.htm for more help
"""

import pytest
from lexer import Lexer
from parser import Parser
from evaluator import Evaluator
from output_formatter import OutputFormatter
from context import Context, SymbolTable

def run_command(str, context=None, return_context=False):
    """
    Helper function which takes a command and returns its output (as a tuple with both
    the raw output and formatted output)
    """
    lexer = Lexer(str)
    lexer.lex()

    parser = Parser(lexer.tokens)
    ast = parser.parse_all()

    evaluator = Evaluator(ast)

    if  context is None:
        context = Context("global_context", symbol_table=SymbolTable())
        # True and False variables
        context.symbol_table.set("ᚷ", False)
        context.symbol_table.set("ᚸ", True)

    result = evaluator.traverse(context)

    formatter = OutputFormatter(result)
    formatted_result = formatter.format()

    if return_context:
        return (result, formatted_result, context)
    else:
        return (result, formatted_result)

@pytest.mark.parametrize(
    "command_str, expected_raw_result, expected_formatted_result",
    [
        ("ᛒ⋅ᛁᛄ.ᛁᛄ⋅ᛚ⋅ᚿ⋅ᛁᛄᛁ⋅ᛚ⋅ᛁᛄᛁ⋅ᚢ⋅ᛒ⋅ᛁᛄᛁ⋅ᛆ", -50.0, "ᛒ⋅ᛁᛁᛄᛄᛁᛄ.ᛄ"), # Arithmetic ops (*, +)
        ("ᚿ⋅ᛁᛁᛄᛁ⋅ᛒ⋅ᛁᛁ⋅ᛆ⋅ᚫ⋅ᛁᛄ", 5.0, "ᛁᛄᛁ.ᛄ"), # Arithmetic ops (/, -) (python div results in float)
        ("ᛁᛄᛁ⋅ᛖ⋅ᛁᛁ⋅ᚢ⋅ᛁᛄ", True, "ᚸ"), # Equals comparison
        ("ᛁᛄᛁ⋅ᛒᛖᛏ⋅ᛁᛁ⋅ᚢ⋅ᛁᛄ", False, "ᚷ"), # More than comparison
        ("ᛁᛄᛁ⋅ᛅᚺᛣ⋅ᛁᛁᛁ⋅ᚢ⋅ᛁᛄ", True, "ᚸ"), # Less than comparison
        ("ᚸ⋅ᛢ⋅ᚸ", True, "ᚸ"), # And boolean
        ("ᚷ⋅ᛢ⋅ᚸ", False, "ᚷ"),
        ("ᚷ⋅ᛖᛏ⋅ᚸ", True, "ᚸ"), # Or boolean
        ("ᚷ⋅ᛖᛏ⋅ᚷ", False, "ᚷ"),
        ("ᛉᛖᛚ⋅ᚿ⋅ᚷ⋅ᛆ", True, "ᚸ"), # Not
        ("ᛉᛖᛚ⋅ᚿ⋅ᚸ⋅ᛆ", False, "ᚷ"),
        ("ᛁᛩ⋅ᚸ\nᛁ\nᚺᛅᛁᛩ⋅ᚷ\nᛁᛄ\nᚺᛅᛣ\nᛁᛁ", 1, "ᛁ"), # If statement
        ("ᛁᛩ⋅ᚷ\nᛁ\nᚺᛅᛁᛩ⋅ᚸ\nᛁᛄ\nᚺᛅᛣ\nᛁᛁ", 2, "ᛁᛄ"),
        ("ᛁᛩ⋅ᚷ\nᛁ\nᚺᛅᛁᛩ⋅ᚷ\nᛁᛄ\nᚺᛅᛣ\nᛁᛁ", 3, "ᛁᛁ"),
        ("ᛧᛧᛩᛟᛉᚴᛧᛧ⋅ᚢ⋅ᛧᛧᛒᛒᛒᛧᛧ", "ᛩᛟᛉᚴᛒᛒᛒ", "ᛩᛟᛉᚴᛒᛒᛒ"), # String
        # List initialisation
        ("ᚺ⋅ᛁᛄᛁ⋅ᛧ⋅ᛁᛄ⋅ᛧ⋅ᛁᛁᛁ⋅ᛧ⋅ᛁᛄ⋅ᚢ⋅ᛁᛄ⋅ᚻ", [5,2,7,4], "ᚺ⋅ᛁᛄᛁ⋅ᛧ⋅ᛁᛄ⋅ᛧ⋅ᛁᛁᛁ⋅ᛧ⋅ᛁᛄᛄ⋅ᚻ"),
        ("ᚺ⋅ᛁᛄᛁ⋅ᛧ⋅ᛁᛄ⋅ᛧ⋅ᛁᛁᛁ⋅ᛧ⋅ᛁᛄ⋅ᚢ⋅ᛁᛄ⋅ᚻ⋅ᛝ⋅ᛁᛄ⋅ᚢ⋅ᛁᛄ", 9, "ᛁᛄᛄᛁ"), # List indexing
        ("ᛉᛟᛒ⋅ᚿ⋅ᛧᛧᛁᛄᛁ.ᛄᛁᛧᛧ⋅ᛆ", 5.25, "ᛁᛄᛁ.ᛄᛁ"), # String to int/float function
        ("ᛣᛠᛝᚹ⋅ᚲ⋅ᛁᛄ.ᛁᛄ⋅ᛚ⋅ᛁᛄ\nᛣᛠᛝᚹ", 5.0, "ᛁᛄᛁ.ᛄ"), # Variable assignment and access
        ("ᛞ⋅ᚷ⋅ᛅᚺᛣ⋅ᛁᛄᛄᛄᛄ\nᚷ⋅ᚲ⋅ᚷ⋅ᚢ⋅ᛁ\n\nᚷ", 16, "ᛁᛄᛄᛄᛄ"), # While loop
        # Function declaration and call
        ("ᛩᛟᛉᚴ⋅ᛒᛒᛒ⋅ᛟ⋅ᛧ⋅ᛟᛟ⋅ᛧ⋅ᛟᛟᛟ\nᛟ⋅ᛚ⋅ᛟᛟ⋅ᛚ⋅ᛟᛟᛟ\n\nᛒᛒᛒ⋅ᚿ⋅ᛁᛄ⋅ᛧ⋅ᛁᛁ⋅ᛧ⋅ᛁᛄᛄ⋅ᛆ", 24, "ᛁᛁᛄᛄᛄ"),
        ("ᛩᛟᛉᚴ⋅ᛒᛒᛒ\nᛧᛧᛩᛟᛉᚴᛧᛧ⋅ᚢ⋅ᛧᛧᛒᛒᛒᛧᛧ\n\nᛒᛒᛒ⋅ᚿ⋅ᛆ", "ᛩᛟᛉᚴᛒᛒᛒ", "ᛩᛟᛉᚴᛒᛒᛒ"), # Function without parameters
        ("ᛣᛠᛝᚹ⋅ᚲ⋅ᚺ⋅ᛁᛄᛁ⋅ᛧ⋅ᛁᛄ⋅ᛧ⋅ᛁᛁᛁ⋅ᛧ⋅ᛁᛄᛁ⋅ᛧ⋅ᛁᛄ⋅ᚻ\nᛅᚺᛉ⋅ᚿ⋅ᛣᛠᛝᚹ⋅ᛆ", 5, "ᛁᛄᛁ")
    ]
)
def test_pipeline_valid_single_command(
    command_str,
    expected_raw_result,
    expected_formatted_result
):
    """
    Tests the entire programming language pipeline with various different fuunctionality
    (if/else statement, loop, variables etc)
    """
    raw_result, formatted_result = run_command(command_str)

    assert raw_result == expected_raw_result
    assert type(raw_result) == type(expected_raw_result)
    assert formatted_result == expected_formatted_result
    assert type(formatted_result) == type(expected_formatted_result)

def test_print_function(capsys):
    """
    Function to test the programming language's print function. This is needed as a
    separate unit test as we are testing for what was printed rather than what was
    returned. capsys is imported to capture the sys.stdout.
    """
    command_str = "ᚹᛏᛁᛉᛚ⋅ᚿ⋅ᛁᛄᛁ⋅ᛆ"
    raw_result, formatted_result = run_command(command_str)
    printed_output = capsys.readouterr().out

    assert printed_output == "ᛁᛄᛁ\n" #/n is needed as that is included by print()

def test_input_function(monkeypatch):
    """
    Function to test the programming language's input function. This is needed as a
    separate unit test as Python's input() function needs mocking (monkeypatching).
    """
    monkeypatch.setattr("builtins.input", lambda _: "ᛣᛐᛒᛝ")
    command_str = "ᛁᛉᚹ⋅ᚿ⋅ᛧᛧᛁᛉᚹᛟᛚᛧᛧ⋅ᛆ" # Input function is called with some prompt text
    raw_result, formatted_result = run_command(command_str)

    assert raw_result == formatted_result == "ᛣᛐᛒᛝ"
