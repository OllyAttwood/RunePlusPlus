"""
Tests native functions.

If the command "pytest" doesn't work (as it didn't for me), use
"python -m pytest" instead.

Run the command from the code/rune++ directory.

See https://www.tutorialspoint.com/pytest/index.htm for more help
"""

import pytest
import native_functions
from errors import RunePlusPlusError

@pytest.mark.parametrize(
    "to_print, expected_output",
    [
        ("ᛁᛄᛁ", "ᛁᛄᛁ"),
        (11, "ᛁᛄᛁᛁ"),
        (3.75, "ᛁᛁ.ᛁᛁ")
    ]
)
def test_print_function(capsys, to_print, expected_output):
    """
    Function to test the programming language's print function. This is needed as a
    separate unit test as we are testing for what was printed rather than what was
    returned. capsys is imported to capture the sys.stdout.
    """
    native_functions.ᚹᛏᛁᛉᛚ(to_print)
    printed_output = capsys.readouterr().out

    assert printed_output == f"{expected_output}\n" #/n is needed as that is included by print()

@pytest.mark.parametrize(
    "to_input",
    [
        "ᛏᚳᛣᚴᚠᛉᚩᛠ",
        "ᛉᚩᛠ",
        "ᚠᛉᚩ",
        ""
    ]
)
def test_input_function_valid(monkeypatch, to_input):
    """Tests the input function with valid inputs"""
    monkeypatch.setattr("builtins.input", lambda _: to_input)
    result = native_functions.ᛁᛉᚹ(to_input)

    assert result == to_input

@pytest.mark.parametrize(
    "to_input",
    [
        "hello",
        "ᛏᚳᛣᚴdᚠᛉᚩᛠ",
        "ᛉᚩ ᛠ",
        "2ᛉᚩ"
    ]
)
def test_input_function_invalid(monkeypatch, to_input):
    """
    Tests the input function with invalid inputs, so an error should be raised.
    Monkeypatch is needed to mock the input function.
    """
    monkeypatch.setattr("builtins.input", lambda _: to_input)

    with pytest.raises(RunePlusPlusError):
        native_functions.ᛁᛉᚹ(to_input)
