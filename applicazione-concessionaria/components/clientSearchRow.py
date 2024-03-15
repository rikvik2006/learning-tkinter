import customtkinter as ctk

from components.ccomboBox import CComboBox
from components.centry import CEntry

class ClientSearchRow(ctk.CTkFrame):
    """Frist row in client tab"""

    def __init__(self, master, layout, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(**layout)
        self.configure(fg_color="transparent")

        self.search_combobox = CComboBox(master=self, values=["Tutti", "Auto Veicoli", "Auto Carri", "Moto Veicoli"])
        self.search_combobox.grid(row=0, column=0)
        self.search_entry = CEntry(master=self, placeholder_text="Cerca")
        self.search_entry.grid(row=0, column=1, padx=(30, 0))
        
        self.__combobox_binding()
    
    def __combobox_binding(self):
        # Dato che il Frame ClientSearchRow viene caricato prima di TableContainerFrame, il frame al quale vogliamo accedere dobbiamo aspettare che la pagina sia completamente caridcata per poterci accedere, altrimenti non sarebbe definito
        def bind_combobox():
            try:
                table_container = self.master.components["table_container_frame"]
                self.search_combobox.bind("<<ComboboxSelected>>", lambda event: self.test_test())
            except KeyError:
                self.after(100, bind_combobox)  # Riprova dopo 100ms

        self.after_idle(bind_combobox)
    
    def test_test(self):
        print("🌟🌟 Ciao")

