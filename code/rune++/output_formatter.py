import number_converter

class OutputFormatter:
    """
    Used to ensure the output is formatted correctly e.g. convert numbers back to runes
    and correctly handle negative numbers
    """

    FORMATTING_MAP = {
        "-": "ᛒ⋅"
    }

    def __init__(self, original_output):
        self.original_output = original_output

    def format(self):
        """
        Ensures the output is formatted correctly e.g. convert numbers back to runes
        and correctly handle negative numbers
        """

        # If original is a number
        if isinstance(self.original_output, (int, float)):
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

        return new_output
