class Presenter:
    """The presenter class to co-ordinate the view with the real functionality"""

    def __init__(self, view, model):
        self.view = view
        self.model = model


        # Setup button callbacks
        self.view.register_open_file_callback(self.model.open_file)
        self.view.register_save_as_callback(self.model.save_to_file)
