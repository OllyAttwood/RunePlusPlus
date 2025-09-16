"""
Tests for the number_converter.py functions.

If the command "pytest" doesn't work (as it didn't for me), use
"python -m pytest" instead.

Run the command from the code/rune++ directory.

See https://www.tutorialspoint.com/pytest/index.htm for more help
"""

import pytest
from number_converter import *
from number_converter import (
    _from_base2_to_base10, _from_base2_fractional_to_base10, _from_base10_to_base2,
    _replace_digits_with_runes, _split_float, _from_base10_fractional_to_base2
)

@pytest.mark.parametrize(
    "input_runes, expected_number",
    [
        ("ᛄ", 0),
        ("ᛁᛄ", 2),
        ("ᛁᛁᛁᛄᛁᛁᛁᛁᛄ", 478),
        ("ᛄᛁᛄᛄᛄᛄᛄᛄᛁ", 129),
        ("ᛁᛄᛁ.ᛁᛄᛁ", 5.625),
        ("ᛄᛁᛄ.ᛄ", 2.0)
    ]
)
def test_from_runes_to_base10(input_runes, expected_number):
    """
    Tests the from_runes_to_base10() function by comparing the converted runes with the
    expected output
    """
    result = from_runes_to_base10(input_runes)

    assert result == expected_number
    assert type(result) == type(expected_number)

@pytest.mark.parametrize(
    "input_number, expected_runes",
    [
        (3, "ᛁᛁ"),
        (0, "ᛄ"),
        (120, "ᛁᛁᛁᛁᛄᛄᛄ"),
        (6.75, "ᛁᛁᛄ.ᛁᛁ"),
        (5.0, "ᛁᛄᛁ.ᛄ")
    ]
)
def test_from_base10_to_runes(input_number, expected_runes):
    """
    Tests the from_base10_to_runes() function by comparing the converted number with the
    expected output runes
    """
    result = from_base10_to_runes(input_number)

    assert result == expected_runes

@pytest.mark.parametrize(
    "input_base2, expected_base10",
    [
        ("1001", 9),
        ("0", 0),
        ("0101", 5)
    ]
)
def test_from_base2_to_base10(input_base2, expected_base10):
    """
    Tests the _from_base2_to_base10() function by comparing the converted base 2 number
    with the expected base 10 number
    """
    result = _from_base2_to_base10(input_base2)

    assert result == expected_base10

@pytest.mark.parametrize(
    "input_base2_fractional, expected_base10_fractional",
    [
        ("011", 375),
        ("0", 0),
        ("100", 5),
        ("11111", 96875)
    ]
)
def test_from_base2_fractional_to_base10(
    input_base2_fractional,
    expected_base10_fractional
):
    """
    Tests the _from_base2_fractional_to_base10() function by comparing the converted
    base 2 fractional number with the expected base 10 number
    """
    result = _from_base2_fractional_to_base10(input_base2_fractional)

    assert result == expected_base10_fractional

@pytest.mark.parametrize(
    "input_base10, expected_base2",
    [
        (22, "10110"),
        (0, "0"),
        (109, "1101101")
    ]
)
def test_from_base10_to_base2(input_base10, expected_base2):
    """
    Tests the _from_base10_to_base2() function by comparing the converted base 10 number
    with the expected base 2 number
    """
    result = _from_base10_to_base2(input_base10)

    assert result == expected_base2

@pytest.mark.parametrize(
    "input_digits, expected_runes",
    [
        ("101010", "ᛁᛄᛁᛄᛁᛄ"),
        ("011", "ᛄᛁᛁ"),
        ("", "")
    ]
)
def test_replace_digits_with_runes(input_digits, expected_runes):
    """
    Tests the _replace_digits_with_runes() function by comparing the converted digits
    with the expected runes
    """
    result = _replace_digits_with_runes(input_digits)

    assert result == expected_runes

@pytest.mark.parametrize(
    "input_float_str, expected_int_str, expected_fractional_str",
    [
        ("12345.6789", "12345", "6789"),
        ("1.0", "1", "0"),
        ("0.372", "0", "372"),
        ("0.0", "0", "0")
    ]
)
def test_split_float(input_float_str, expected_int_str, expected_fractional_str):
    """
    Tests the _split_float() function by comparing the split digits with the expected
    outputs
    """
    int_result, fractional_result = _split_float(input_float_str)

    assert int_result == expected_int_str
    assert fractional_result == expected_fractional_str

@pytest.mark.parametrize(
    "input_base10_fractional, expected_base2",
    [
        ("75", "11"),
        ("15625", "00101"),
        ("0", "0")
    ]
)
def test_from_base10_fractional_to_base2(input_base10_fractional, expected_base2):
    """
    Tests the _from_base10_fractional_to_base2() function by comparing the converted
    base 10 fractional digits with the expected base 2 digits
    """
    result = _from_base10_fractional_to_base2(input_base10_fractional)

    assert result == expected_base2
