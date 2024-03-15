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
        
        
    def __load_layout(self):
        for name, component, layout in self.layout:
            self.components[name] = component(master=self, layout=layout)
                
    def __load_dummy_data(self):
        self.__concessionaria.add_motoveicolo("XV 934 ML", "Kawasaki", "Kawasaki Ninja", 2, 4974.75, 816)
        self.__concessionaria.add_motoveicolo("EJ 754 SM", "Kawasaki", "Kawasaki YZF-R", 1, 11998.69, 1063)
        self.__concessionaria.add_autoveicolo("XN 144 AI", "Volkswagen", "Volkswagen Golf", 2, 13613.85, 3)
        self.__concessionaria.add_autoveicolo("AV 501 JT", "Volkswagen", "Volkswagen Panda", 5, 17787.87, 5)
        self.__concessionaria.add_autoveicolo("NU 557 EA", "Ford", "Ford Focus", 2, 9670.4, 5)
        self.__concessionaria.add_autocarro("NE 759 BC", "MAN", "MAN Eurocargo", 2, 42081.67, 2997)
        self.__concessionaria.add_motoveicolo("FM 893 SF", "Honda", "Honda Ninja", 1, 5739.09, 380)
        self.__concessionaria.add_autoveicolo("MP 098 VN", "Renault", "Renault Panda", 4, 25730.94, 3)
        self.__concessionaria.add_autoveicolo("OS 193 QO", "Ford", "Ford Focus", 2, 12638.76, 5)
        self.__concessionaria.add_autoveicolo("WO 382 HO", "Toyota", "Toyota Golf", 4, 14716.73, 3)
        self.__concessionaria.add_motoveicolo("ZJ 081 CO", "Honda", "Honda GSX-R", 1, 7384.33, 128)
        self.__concessionaria.add_autoveicolo("XT 263 AM", "Fiat", "Fiat Golf", 4, 24111.74, 5)
        self.__concessionaria.add_autoveicolo("YB 538 BO", "Toyota", "Toyota Panda", 3, 8544.43, 3)
        self.__concessionaria.add_motoveicolo("KR 329 XY", "Yamaha", "Yamaha CBR", 1, 6442.67, 329)
        self.__concessionaria.add_autoveicolo("KA 110 EN", "Volkswagen", "Volkswagen Focus", 2, 15107.9, 3)
        self.__concessionaria.add_motoveicolo("AQ 869 JZ", "Suzuki", "Suzuki CBR", 2, 7334.49, 331)
        self.__concessionaria.add_autoveicolo("GH 228 KT", "Fiat", "Fiat Panda", 5, 14524.4, 3)
        self.__concessionaria.add_autocarro("YA 793 FA", "MAN", "MAN Actros", 2, 65586.23, 1218)
        self.__concessionaria.add_autoveicolo("UB 978 IX", "Volkswagen", "Volkswagen Panda", 3, 11783.17, 4)

            

# Default font: {'family': 'Segoe UI', 'size': 9, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
if __name__ == "__main__":
    app = App(Concessionaria())
    app.mainloop()
