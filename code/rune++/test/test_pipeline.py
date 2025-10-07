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

    parser = Parser(lexer.tokens[0])
    ast = parser.parse_line()

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
        ("ᛒ⋅ᛁᛄ.ᛁᛄ⋅ᛚ⋅ᚿ⋅ᛁᛄᛁ⋅ᛚ⋅ᛁᛄᛁ⋅ᚢ⋅ᛒ⋅ᛁᛄᛁ⋅ᛆ", -50.0, "ᛒ⋅ᛁᛁᛄᛄᛁᛄ.ᛄ"), # Arithmetic ops
        ("ᛁᛄᛁ⋅ᛖ⋅ᛁᛁ⋅ᚢ⋅ᛁᛄ", True, "ᚸ"), # Equals comparison
        ("ᛁᛄᛁ⋅ᛒᛖᛏ⋅ᛁᛁ⋅ᚢ⋅ᛁᛄ", False, "ᚷ"), # More than comparison
        ("ᛁᛄᛁ⋅ᛅᚺᛣ⋅ᛁᛁᛁ⋅ᚢ⋅ᛁᛄ", True, "ᚸ"), # Less than comparison
        ("ᚸ⋅ᛢ⋅ᚸ", True, "ᚸ"), # And boolean
        ("ᚷ⋅ᛢ⋅ᚸ", False, "ᚷ"),
        ("ᚷ⋅ᛖᛏ⋅ᚸ", True, "ᚸ"), # Or boolean
        ("ᚷ⋅ᛖᛏ⋅ᚷ", False, "ᚷ"),
        ("ᛁᛩ⋅ᚸ⋅⋮⋅ᛁ⋅ᚺᛅᛁᛩ⋅ᚷ⋅⋮⋅ᛁᛄ⋅ᚺᛅᛣ⋅ᛁᛁ", 1, "ᛁ"), # If statement
        ("ᛁᛩ⋅ᚷ⋅⋮⋅ᛁ⋅ᚺᛅᛁᛩ⋅ᚸ⋅⋮⋅ᛁᛄ⋅ᚺᛅᛣ⋅ᛁᛁ", 2, "ᛁᛄ"),
        ("ᛁᛩ⋅ᚷ⋅⋮⋅ᛁ⋅ᚺᛅᛁᛩ⋅ᚷ⋅⋮⋅ᛁᛄ⋅ᚺᛅᛣ⋅ᛁᛁ", 3, "ᛁᛁ"),
        ("ᛧᛧᛩᛟᛉᚴᛧᛧ⋅ᚢ⋅ᛧᛧᛒᛒᛒᛧᛧ", "ᛩᛟᛉᚴᛒᛒᛒ", "ᛩᛟᛉᚴᛒᛒᛒ"), # String
        # List initialisation
        ("ᚺ⋅ᛁᛄᛁ⋅ᛧ⋅ᛁᛄ⋅ᛧ⋅ᛁᛁᛁ⋅ᛧ⋅ᛁᛄ⋅ᚢ⋅ᛁᛄ⋅ᚻ", [5,2,7,4], "ᚺ⋅ᛁᛄᛁ⋅ᛧ⋅ᛁᛄ⋅ᛧ⋅ᛁᛁᛁ⋅ᛧ⋅ᛁᛄᛄ⋅ᚻ"),
        ("ᚺ⋅ᛁᛄᛁ⋅ᛧ⋅ᛁᛄ⋅ᛧ⋅ᛁᛁᛁ⋅ᛧ⋅ᛁᛄ⋅ᚢ⋅ᛁᛄ⋅ᚻ⋅ᛝ⋅ᛁᛄ⋅ᚢ⋅ᛁᛄ", 9, "ᛁᛄᛄᛁ") # List indexing
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

@pytest.mark.parametrize(
    "command_str_list, expected_raw_result, expected_formatted_result",
    [
        (["ᛣᛠᛝᚹ⋅ᚲ⋅ᛁᛄ.ᛁᛄ⋅ᛚ⋅ᛁᛄ", "ᛣᛠᛝᚹ"], 5.0, "ᛁᛄᛁ.ᛄ"), # Variable assignment and access
        (["ᛞ⋅ᚷ⋅ᛅᚺᛣ⋅ᛁᛄᛄᛄᛄ⋅⋮⋅ᚷ⋅ᚲ⋅ᚷ⋅ᚢ⋅ᛁ", "ᚷ"], 16, "ᛁᛄᛄᛄᛄ"), # While loop
        (
            ["ᛩᛟᛉᚴ⋅ᛒᛒᛒ⋅ᛟ⋅ᛧ⋅ᛟᛟ⋅ᛧ⋅ᛟᛟᛟ⋅⋮⋅ᛟ⋅ᛚ⋅ᛟᛟ⋅ᛚ⋅ᛟᛟᛟ", "ᛒᛒᛒ⋅ᚿ⋅ᛁᛄ⋅ᛧ⋅ᛁᛁ⋅ᛧ⋅ᛁᛄᛄ⋅ᛆ"],
            24,
            "ᛁᛁᛄᛄᛄ"
        )                                             # Function declaration and call
    ]
)
def test_pipeline_valid_multi_commands(
    command_str_list,
    expected_raw_result,
    expected_formatted_result
):
    """
    Tests the entire programming language pipeline with multiple commands, executed
    sequentially. Needed for testing the symbol table has been updated.
    """
    raw_output, formatted_output, context = run_command(
        command_str_list[0],
        return_context=True
    )

    for command_str in command_str_list[1:]:
        raw_output, formatted_output = run_command(
            command_str,
            context=context
        )

    assert raw_output == expected_raw_result
    assert type(raw_output) == type(expected_raw_result)
    assert formatted_output == expected_formatted_result
    assert type(formatted_output) == type(expected_formatted_result)

def test_print_function(capsys):
    """
    Function to test the programming languages print function. This is needed as a
    separate unit test as we are testing for what was printed rather than what was
    returned. capsys is imported to capture the sys.stdout.
    """
    command_str = "ᚹᛏᛁᛉᛚ⋅ᚿ⋅ᛁᛄᛁ⋅ᛆ"
    raw_result, formatted_result = run_command(command_str)
    printed_output = capsys.readouterr().out

    assert printed_output == "ᛁᛄᛁ\n" #/n is needed as that is included by print()
