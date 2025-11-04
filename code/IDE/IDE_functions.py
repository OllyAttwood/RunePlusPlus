class IDE_Functions:
    """
    Class which serves as the model component of the MVP pattern. This contains all the
    functionality and attributes needed for the IDE.
    """

    def __init__(self):
        self.current_file_name = ""

    def open_file(self, file_path):
        """
        Returns the text from the file at the given location, also updates
        current_file_name
        """
        with open(file_path) as open_file:
            file_contents = open_file.read()

        self.current_file_name = file_path

        return file_contents

    def save_to_file(self, file_path, text_to_save):
        """
        Saves the text to the given file location, also updates current_file_name
        """
        with open(file_path, "w") as open_file:
            open_file.write(text_to_save)

        self.current_file_name = file_path

    def save_to_current_file(self, text_to_save):
        """
        Saves the text to the current file location, also updates current_file_name
        """
        if self.current_file_name == "" or self.current_file_name is None:
            raise ValueError("No current file to save to")

        self.save_to_file(self.current_file_name, text_to_save)
