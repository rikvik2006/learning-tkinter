import customtkinter as ctk

from components.ccomboBox import CComboBox
from components.centry import CEntry

class ClientSearchRow(ctk.CTkFrame):
    """Frist row in client tab"""

    def __init__(self, master, layout, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(**layout)
        self.configure(fg_color="transparent")

        self.search_combobox = CComboBox(master=self, values=["Auto Veicoli", "Auto Carri", "Moto Veicoli"])
        self.search_combobox.grid(row=0, column=0)
        self.search_entry = CEntry(master=self, placeholder_text="Cerca")
        self.search_entry.grid(row=0, column=1, padx=(30, 0))