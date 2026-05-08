import customtkinter as ctk

class Tooltip:
    """A tooltip for a single widget."""

    # How far the tooltip should be from the cursor
    TOOLTIP_OFFSET = 10
    TOOLTIP_FONT_SIZE = 17
    TOOLTIP_PADDING = 20

    def __init__(self, widget, text, outer_container):
        """Set up mouse bindings."""
        self.widget = widget
        self.text = text
        self.outer_container = outer_container
        self.label = None

        # Create bindings for mouse movement
        widget.bind("<Enter>", self.on_mouse_enter)
        widget.bind("<Motion>", self.on_mouse_motion)
        widget.bind("<Leave>", self.on_mouse_leave)

    def on_mouse_enter(self, event):
        """Sets up the new tooltip if any previous tooltip has been destroyed."""
        if not self.label:
            self.label = ctk.CTkLabel(
                self.outer_container, 
                text=self.text, 
                font=(None, self.TOOLTIP_FONT_SIZE),
                padx=self.TOOLTIP_PADDING
            )

    def on_mouse_motion(self, event):
        """Moves the tooltip with the user cursor"""
        if self.label:
            # Co-ordinates are calculated relative to the keyboard frame and entire 
            # window
            x = event.x_root - self.outer_container.winfo_rootx() + self.TOOLTIP_OFFSET
            y = event.y_root - self.outer_container.winfo_rooty() + self.TOOLTIP_OFFSET
            
            self.label.place(x=x, y=y)

    def on_mouse_leave(self, event):
        """
        Checks that cursor has actually left the widget (not just a label widget within 
        it), and destroys the tooltip if so.
        """
        if self.label and self.cursor_outside_widget(event):
            self.label.destroy()
            self.label = None

    def cursor_outside_widget(self, event):
        """Checks if the cursor is outside the tooltip's parent widget."""
        # Cursor location
        absolute_x = event.x_root
        absolute_y = event.y_root

        # Widget bounds
        x_lower_limit = self.widget.winfo_rootx()
        y_lower_limit = self.widget.winfo_rooty()
        x_upper_limit = x_lower_limit + self.widget.winfo_width()
        y_upper_limit = y_lower_limit + self.widget.winfo_height()

        return (
            absolute_x < x_lower_limit or absolute_x >= x_upper_limit
            or absolute_y < y_lower_limit or absolute_y >= y_upper_limit
        )
