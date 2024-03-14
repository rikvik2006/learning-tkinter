import customtkinter as ctk

class CComboBox(ctk.CTkComboBox):
    """Styled combo box"""

    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        self.configure(width=200, height=40, button_color="#33333A", fg_color="#33333A", dropdown_fg_color="#33333A", border_width=0, text_color="#7B7B80", corner_radius=12, button_hover_color="#3A3A3A", dropdown_text_color="#7B7B80", font=("Segoe UI Semibold", 15))
