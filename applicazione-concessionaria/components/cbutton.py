from cgitb import text
import customtkinter as ctk
from typing import Any

class CButton(ctk.CTkButton):
    """A styled custom button"""

    def __init__(self, master: Any, **kwargs):
        super().__init__(master=master, **kwargs)
        self.__configure_style()
        
    def __configure_style(self): 
        self.configure(fg_color="#33333A", font=("Segoe UI Semibold", 17), border_spacing=15, corner_radius=12, border_color="#3A3A3A", border_width=4, hover_color="#2B2B31")

