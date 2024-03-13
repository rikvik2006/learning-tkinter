import tkinter as tk
from typing import Tuple, Any
import customtkinter as ctk
from components.tabViewFrame import TabViewFrame
from utils.types import LayoutPositionGrid

from tkinter import font



class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        ctk.set_appearance_mode("dark")
        self.configure(fg_color="#282830", padx=25, pady=25)
        self.__define_layout()
        self.__load_layout()
        
    def __define_layout(self):
        self.layout = [
            [
                "tab_view",
                TabViewFrame,
                LayoutPositionGrid(row=0, column=0, sticky="nsew")(),
            ]
        ]
        
        
    def __load_layout(self):
        self.components = {}
        for name, component, layout in self.layout:
            self.components[name] = component(master=self, layout=layout)
        # self.test = TabViewFrame(master=self)
        # self.test.grid(row=0, column=0)
                

            

# Default font: {'family': 'Segoe UI', 'size': 9, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
if __name__ == "__main__":
    app = App()
    app.mainloop()
