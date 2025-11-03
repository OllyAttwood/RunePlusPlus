class Presenter:
    """The presenter class to co-ordinate the view with the real functionality"""

    def __init__(self, view, model):
        self.view = view
        self.model = model
