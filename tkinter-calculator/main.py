import tkinter as tk
from tkinter import Button, ttk
from utils.types import LayoutPositionGrid
from components.CalculatorButton import CalculatorButton
from components.ButtonsFrame import ButtonsFrame
from components.DisplayFrame import DisplayFrame
from components.InfoDisplay import InfoDisplayFrame
from components.CalculatorSelector import CalculatorSelector
from hooks.memory import Memory
from constants import STANDARD_CALCULATOR_BUTTONS, SCIENTIFIC_CALCULATOR_BUTTONS


class App(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.style = ttk.Style()
        self.configure_style()
        self.title("Black Calculator")

        self.layout = [
            [
                "info_display",
                InfoDisplayFrame,
                LayoutPositionGrid(row=0, column=0, sticky="nsew")(),
            ],
            [
                "display",
                DisplayFrame,
                LayoutPositionGrid(row=1, column=0, sticky="nsew")(),
            ],
            [
                "calculator_selector",
                CalculatorSelector,
                LayoutPositionGrid(row=2, column=0, sticky="nesw")(),
            ],
        ]

        # Lista di ButtonFrame, contiene i bottone di ogni calcolatrice, questo ci permette quindi di cambiare calcualtrice
        self.calculator: list[ButtonsFrame] = []
        self.calculator.append(
            ButtonsFrame(
                master=self,
                layout=LayoutPositionGrid(row=3, column=0, sticky="nesw")(),
                buttons=STANDARD_CALCULATOR_BUTTONS,
                style="App.TFrame",
            )
        )
        self.calculator.append(
            ButtonsFrame(
                master=self,
                layout=LayoutPositionGrid(row=3, column=0, sticky="nesw")(),
                buttons=SCIENTIFIC_CALCULATOR_BUTTONS,
                style="App.TFrame",
            )
        )
        # Essendo nella stessa cella della griglia, "tiriamo su", la calcolatrice standard per mostrarla
        self.calculator[0].tkraise()

        self.components = {}
        self.create_layout()
        self.initialize_memory_manager()

    def create_layout(self):
        for name, component, layout in self.layout:
            self.components[name] = component(
                master=self, layout=layout, style="App.TFrame"
            )

    def configure_style(self):
        self.style.theme_use("alt")
        self.style.configure("App.TFrame", background="#1D1D1D")
        self.configure(background="#202020")

    def initialize_memory_manager(self):
        # Instaziamo una classe memoria per l'intera calcolatrice, dato che ogni calcoaltrice ha una sola memoria
        self.memory = Memory(master=self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
