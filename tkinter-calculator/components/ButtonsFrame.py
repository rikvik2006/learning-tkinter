import tkinter as Tk
from multiprocessing import set_forkserver_preload
from tkinter import ttk
from components.CalculatorButton import CalculatorButton


class ButtonsFrame(ttk.Frame):
    def __init__(self, master, layout, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(**layout)
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

        self.widget_buttons = []

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
                    # command=lambda text=button_text: self.master.components[
                    #     "display"
                    # ].add_text(text),
                )
                button.grid(row=row_index, column=column_index, sticky="nsew")
                self.widget_buttons.append(button)

                # Aggiungo al bottone l'evento di click con il tasto sinitro del mouse
                button.bind("<Button-1>", lambda event: self.on_click(event=event))

    # Metodo di callback per l'evento di click con il tasto sinitro del mouse di un bottone
    def on_click(self, event: Tk.Event):
        # In base al testo del bottone eseguiamo l'azione corrispondente
        display = self.master.components["display"]
        if event.widget["text"] == "C":
            display.clear()
        elif event.widget["text"] == "=":
            pass
        elif event.widget["text"] == "BC":
            display.backspace()
        elif event.widget["text"] == "MEM":
            self.__display_memory()
        elif event.widget["text"] == "STO":
            self.__store_to_memory()
        elif event.widget["text"] == "M+":
            self.__add_to_memory()
        else:
            display.add_text(event.widget["text"])

    def __display_memory(self):
        memory_number = self.master.memory.get_memory()
        print("📝 Memory number", memory_number)

    def __store_to_memory(self):
        pass

    def __add_to_memory(self):
        pass
