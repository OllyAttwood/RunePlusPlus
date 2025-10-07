import number_converter
import token_map

class OutputFormatter:
    """
    Used to ensure the output is formatted correctly e.g. convert numbers back to runes
    and correctly handle negative numbers
    """

    FORMATTING_MAP = {
        "-": "ᛒ⋅",
        False: "ᚷ",
        True: "ᚸ",
        None: "ᛉᛟᛉ"
    }

    def __init__(self, original_output):
        self.original_output = original_output

    def format(self):
        """
        Ensures the output is formatted correctly e.g. convert numbers back to runes
        and correctly handle negative numbers
        """
        if self.original_output is None:
            new_output = self.FORMATTING_MAP[self.original_output]

        # If original is a boolean
        elif isinstance(self.original_output, bool):
            new_output = self.FORMATTING_MAP[self.original_output]

        # If original is a number
        elif isinstance(self.original_output, (int, float)):
            new_output = self.original_output

            # If negative, remove minus symbol for now, as number_converter doesn't
            # handle negatives
            if self.original_output < 0:
                is_negative = True
                new_output *= -1
            else:
                is_negative = False

            new_output = number_converter.from_base10_to_runes(new_output)

            # If negative, restore (rune version of) minus symbol
            if is_negative:
                new_output = self.FORMATTING_MAP["-"] + new_output

        # If original is a list
        elif isinstance(self.original_output, list):
            new_output = list_to_str(self.original_output)

        # If original is already valid rune characters
        elif (
            isinstance(self.original_output, str)
            and set(self.original_output) <= set(token_map.VARIABLE_NAME_CHARS)
        ):
            new_output = self.original_output

        return new_output

def list_to_str(original_list):
    """
    Converts a list into a correctly formatted string representation (also has to format
    each element)
    """
    comma_and_separators = "⋅ᛧ⋅"
    rune_str = "ᚺ⋅"

    for element in original_list:
        new_formatter = OutputFormatter(element)
        rune_str += new_formatter.format() + comma_and_separators

    # Trim trailing comma
    if len(original_list) > 0:
        rune_str = rune_str[:-len(comma_and_separators)]

    rune_str += "⋅ᚻ"

    return rune_str
