import customtkinter as ctk
from components.cbutton import CButton

class TabViewFrame(ctk.CTkFrame):
    def __init__(self, master, layout, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(**layout)
        self.__set_style()
        
        client_button = CButton(master=self, text="Cliente")
        operator_button = CButton(master=self, text="Operatore")
        client_button.grid(row=0, column=0, padx=(0, 15))
        operator_button.grid(row=0, column=1)   

    def __set_style(self): 
        self.configure(fg_color="#282830")