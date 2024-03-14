import tkinter as tk
from typing import Tuple, Any
import customtkinter as ctk

from components.tabViewFrame import TabViewFrame
from components.clientTabFrame import ClientTabFrame
from components.operatorTabFrame import OperatorTabFrame
from utils.types import LayoutPositionGrid
from classes.concessionaria import Concessionaria


class App(ctk.CTk):
    def __init__(self, concessionaria: Concessionaria, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        ctk.set_appearance_mode("dark")
        self.configure(fg_color="#282830", padx=25, pady=25)
        self.__set_concessionaria(concessionaria)        
        self.__load_dummy_data()
        self.components = {}
        self.__define_layout()
        self.__load_layout()
        self.components["tab_view"].ungrid_operator_frame()
        
        
    def __define_layout(self):
        self.layout = [
            [
                "tab_view",
                TabViewFrame,
                LayoutPositionGrid(row=0, column=0, sticky="nsew")(),
            ],
            [
                "client_tab",
                ClientTabFrame,
                LayoutPositionGrid(row=1, column=0, sticky="nsew")(),
            ],
            [
                "operator_tab",
                OperatorTabFrame,
                LayoutPositionGrid(row=1, column=0, sticky="nsew")(),
            ]
        ]

    def __set_concessionaria(self, concessionaria: Concessionaria) -> None:
        if (not isinstance(concessionaria, Concessionaria)):
            raise ValueError("devi inserire un oggetto di tipo Concessionaria")
        
        self.__concessionaria = concessionaria
    
    def get_concessionaria(self) -> Concessionaria:
        return self.__concessionaria

    def __load_dummy_data(self):
        for i in range(0, 3):
           self.__concessionaria.add_autoveicolo("AB 013 CF", "Smart", "Smart Eletrica 500", 4, float(7500),  3)
           self.__concessionaria.add_motoveicolo("CA 22O NE", "Piagio", "Piagio di Maradona", 2, 23.3, 150)
           self.__concessionaria.add_autocarro("GG 104 FR", "Piagio", "Piagio di Maradona", 2, 23.3, 150)
        
    def __load_layout(self):
        for name, component, layout in self.layout:
            self.components[name] = component(master=self, layout=layout)
                

            

# Default font: {'family': 'Segoe UI', 'size': 9, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
if __name__ == "__main__":
    app = App(Concessionaria())
    app.mainloop()
