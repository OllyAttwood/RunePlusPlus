"""
Used to convert rune numbers (base 2) to python-friendly data-types (base 10) and vice
versa
"""

DECIMAL_POINT = "."

DIGIT_MAP = {
    "ᛄ": "0",
    "ᛁ": "1",
    "0": "ᛄ",
    "1": "ᛁ"
}

def from_runes_to_base10(rune_str):
    """
    Convert rune numbers to an integer or float (base 10), e.g 'ᛁᛄᛁᛄ.ᛄᛁᛄᛁ' -> 10.3125.
    Note that negative symbol is not handled here as that is handled by the evaluator as
    a unary operator.
    """
    number_str = rune_str.replace("ᛄ", DIGIT_MAP["ᛄ"])
    number_str = number_str.replace("ᛁ", DIGIT_MAP["ᛁ"])
    is_int = "." not in number_str

    if is_int:
        return _from_base2_to_base10(number_str)
    else: # Float
        # Split number up into bits before and after decimal point
        int_portion, fractional_portion = _split_float(number_str)
        # Convert parts separately as fractional part can't be converted using int()
        int_portion_base10 = str(_from_base2_to_base10(int_portion))
        fractional_portion_base10 = str(
            _from_base2_fractional_to_base10(fractional_portion)
        )
        # Re-combine parts
        base10_str = f"{int_portion_base10}{DECIMAL_POINT}{fractional_portion_base10}"

        return float(base10_str)

def from_base10_to_runes(number):
    """
    Convert an integer or float (base 10) to rune numbers (base 2 string), e.g
    10.3125 -> 'ᛁᛄᛁᛄ.ᛄᛁᛄᛁ'
    """
    if isinstance(number, int):
        base2_digits = _from_base10_to_base2(number)
        runes = _replace_digits_with_runes(base2_digits)

        return runes
    else: # Float
        # Split number up into bits before and after decimal point
        int_portion, fractional_portion = _split_float(str(number))
        # Convert parts separately as fractional part can't be converted using bin()
        int_portion_base2 = _from_base10_to_base2(int(int_portion))
        fractional_portion_base2 = str(
            _from_base10_fractional_to_base2(fractional_portion)
        )
        # Re-combine parts
        base2_str = f"{int_portion_base2}{DECIMAL_POINT}{fractional_portion_base2}"
        # Swap 0s and 1s for runes
        runes = _replace_digits_with_runes(base2_str)

        return runes

def _from_base2_to_base10(base2_str):
    """
    Converts regular base 2 number (0 and 1 digits, no floats, just ints) to regular
    base 10 number (0-9 digits)
    """
    return int(base2_str, base=2)

def _from_base2_fractional_to_base10(base2_str):
    """
    Converts the fractional part (after the decimal point) of a base 2 number (0 and 1
    digits) to regular base 10 number (0-9 digits)
    """
    multiplier = 1
    total = 0

    for digit in base2_str:
        multiplier /= 2
        total += int(digit) * multiplier # 0 or 1 times the multiplier

    # remove "0." from start of number
    total = int(str(total)[2:])

    return total

def _from_base10_to_base2(number):
    """
    Converts regular base 10 number (0-9 digits, no floats, just ints) to regular base 2
    number (0 and 1 digits) - returns as str
    """
    return bin(number)[2:] # Trims '0b' from start of str

def _replace_digits_with_runes(number):
    """Replaces 0s and 1s with corresponding runes"""
    runes = number.replace("0", DIGIT_MAP["0"])
    runes = runes.replace("1", DIGIT_MAP["1"])

    return runes

def _split_float(number_str):
    """Splits a number into two parts - the integer part and the fractional part"""
    decimal_point_index = number_str.find(DECIMAL_POINT)
    int_portion = number_str[0:decimal_point_index]
    fractional_portion = number_str[decimal_point_index+1:]

    return int_portion, fractional_portion

def _from_base10_fractional_to_base2(base10_str):
    """
    Converts the fractional part (after the decimal point) of a base 10 number to
    regular base 2 number (0-9 digits)
    """
    if base10_str == "0":
        return "0"

    base10_num = float("0." + base10_str)

    multiplier = 1
    fractional_str = ""

    while base10_num > 0:
        multiplier /= 2

        if multiplier <= base10_num:
            base10_num -= multiplier
            fractional_str += "1"
        else:
            fractional_str += "0"

    return fractional_str
