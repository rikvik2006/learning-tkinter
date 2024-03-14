import customtkinter as ctk

class CEntry(ctk.CTkEntry):
    """Styled CTKEntry"""

    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(width=200, height=40, text_color="#7B7B80", border_width=0, corner_radius=12, fg_color="#33333A", font=("Segoe UI Semibold", 15))