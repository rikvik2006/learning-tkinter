import customtkinter as ctk

from components.clientSearchRow import ClientSearchRow 
from utils.types import LayoutPositionGrid

class ClientTabFrame(ctk.CTkFrame):
    """Frame shown when the client tab is selected"""

    def __init__(self, master, layout, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(**layout, pady=(37, 0))
        self.components = {}
        self.configure(fg_color="transparent")
        self.__define_layout()
        self.__load_layout()
        
    def __define_layout(self):
        self.layout = [
            [
                "client_search_row",
                ClientSearchRow,
                LayoutPositionGrid(row=0, column=0, sticky="nsew")(),
            ],
        ]
        
        
    def __load_layout(self):
        for name, component, layout in self.layout:
            self.components[name] = component(master=self, layout=layout)