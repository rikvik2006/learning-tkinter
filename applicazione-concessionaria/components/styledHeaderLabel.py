import customtkinter as ctk

class StyledHeaderLabel(ctk.CTkLabel):
    """Rappresent a styled label for header"""

    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(fg_color="#33333A", text_color="#7B7B80", corner_radius=12, font=("Segoe UI Semibold", 15))

        if (not "height" in kwargs.keys()): 
            self.configure(height=40)