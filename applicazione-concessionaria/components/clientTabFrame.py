import customtkinter as ctk

from components.clientSearchRow import ClientSearchRow 
from components.numberOfVeicle import NumberOfVeicle
from components.tableHeaderFrame import TableHeaderFrame
from utils.types import LayoutPositionGrid

from components.cbutton import CButton


class ClientTabFrame(ctk.CTkFrame):
    """Frame shown when the client tab is selected"""

    def __init__(self, master, layout, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(**layout, pady=(37, 0))
        self.components = {}
        self.configure(fg_color="transparent")
        self.__define_layout()
        self.__load_layout()

        # Change number: command=lambda: self.components["number_of_veicle"].update_number(12)
        # self.test_button = CButton(self, text="Change number", )
        # self.test_button.grid(row=2, column=0)
        
    def __define_layout(self):
        self.layout = [
            [
                "client_search_row",
                ClientSearchRow,
                LayoutPositionGrid(row=0, column=0, sticky="nsew")(),
            ],
            [
                "number_of_veicle",
                NumberOfVeicle,
                LayoutPositionGrid(row=1, column=0, sticky="nsew")(),
            ],
            [
                "table_header_frame",
                TableHeaderFrame,
                LayoutPositionGrid(row=2, column=0, sticky="nsew")(),
            ]
        ]
        
        
    def __load_layout(self):
        for name, component, layout in self.layout:
            self.components[name] = component(master=self, layout=layout)