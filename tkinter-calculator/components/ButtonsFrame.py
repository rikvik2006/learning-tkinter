from multiprocessing import set_forkserver_preload
from tkinter import ttk
from components.CalculatorButton import CalculatorButton

class ButtonsFrame(ttk.Frame):
    def __init__(self, master, layout, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=1, column=0, sticky="nsew")
        self.create_buttons()

    def create_buttons(self):
        self.buttons = [
            ["MEM", "STO", "M+", "C"],
            ["7", "8", "9", "BC"],
            ["4", "5", "6", "/"],
            ["1", "2", "3", "*"],
            ["0", ".", "+", "-"],
            ["(", ")", "="],
        ]

        # for row_index, row in enumerate(self.buttons):
        #     for column_index, button_text in enumerate(row):
        #         button = ttk.Button(
        #             master=self,
        #             text=button_text,
        #             style="Buttons.TButton",
        #             command=lambda text=button_text: self.master.display.add_text(text),
        #         )
        #         button.grid(row=row_index, column=column_index, sticky="nsew")

        for row_index, row in enumerate(self.buttons):
            for column_index, button_text in enumerate(row):
                button = CalculatorButton(
                    master=self,
                    text=button_text,
                    style="Buttons.TButton",
                    command=lambda text=button_text: self.master.display.add_text(text),
                )
                button.grid(row=row_index, column=column_index, sticky="nsew")