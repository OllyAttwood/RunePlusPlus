class OutputRedirector:
    """Redirects the output from the terminal to the given function"""

    def __init__(self, redirect_func):
        self.redirect_func = redirect_func

    def write(self, text):
        """This method is called whenever any output is produced by the program"""
        self.redirect_func(text)

    def flush(self):
        """Needed for Python's stdout interface"""
        pass
