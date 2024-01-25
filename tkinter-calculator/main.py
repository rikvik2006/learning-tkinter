import tkinter as tk
from tkinter import Button, ttk
from utils.types import LayoutPositionGrid
from components.CalculatorButton import CalculatorButton
from components.ButtonsFrame import ButtonsFrame
from components.DisplayFrame import DisplayFrame


class App(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.style = ttk.Style()
        self.configure_style()

        self.layout = [
            [
                "display",
                DisplayFrame,
                LayoutPositionGrid(row=0, column=0, sticky="nsew")(),
            ],
            [
                "button_frame",
                ButtonsFrame,
                LayoutPositionGrid(row=1, column=0, sticky="nesw")(),
            ],
        ]
        self.components = {}
        self.create_layout()

    def create_layout(self):
        for name, component, layout in self.layout:
            self.components[name] = component(master=self, layout=layout)

    def configure_style(self):
        self.style.theme_use("alt")
        self.style.configure("App.TFrame", background="#1D1D1D")
        self.configure(background="#202020")


if __name__ == "__main__":
    app = App()
    app.mainloop()
