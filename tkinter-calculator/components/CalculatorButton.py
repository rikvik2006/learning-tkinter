from tkinter import ttk

class CalculatorButton(ttk.Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)