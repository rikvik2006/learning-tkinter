import tkinter as Tk
from tkinter import ttk
from components.CalculatorButton import CalculatorButton
from utils.helpers.expression import Expression


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

    # Mostra il contenuto della memoria sul display
    def __display_memory(self):
        memory_number = self.master.memory.get_memory()
        display = self.master.components["display"]

        # Se il display è vuoto quindi contiene 0 il contenuto della memoria sotituisce lo 0.
        # Se l'ultimo carattere del display è un operatore il contenuto della memoria viene aggiunto al display.
        # Altrimenti se nel display è presente un numero oppure un numero incompleto, il contenuto della memoria viene sotiutito al contenuto attuale
        if display.get_text() == "0":
            display.set_text(str(memory_number))
        elif Expression.is_operator(display.get_text()[-1]):
            if memory_number < 0:
                display.add_text("(" + str(memory_number) + ")")
            else:
                display.add_text(str(memory_number))
        else:
            display.set_text(str(memory_number))

        print("📝 Memory number", memory_number)

    # Salva il numero attuale nel display nella memoria (se è presente una espressione viene salvato solo l'ultimo numero)
    def __store_to_memory(self):
        display = self.master.components["display"]
        memory = self.master.memory
        display_current_text = display.get_text()
        numbers = Expression.get_expressions_numbers(display_current_text)
        print("☕", numbers)
        memory.set_memory(numbers[-1])
        print("🔗 Saved value", memory.get_memory())

    # Esegue una somma algebrica con il numero contenuto in memoria e quello mostrato nel display
    # (se è presente una espressione viene sommato solo l'ultimo numero con il contenuto della memoria)
    # TODO: Se il numero è negativo non deve essere sommato ma deve essere sotratto
    # Il problema è che al numero viene rimosso il suo segno, quindi non sappaimo se è positivo o negativo
    def __add_to_memory(self):
        display = self.master.components["display"]
        memory = self.master.memory
        display_current_text = display.get_text()
        numbers = Expression.get_expressions_numbers(display_current_text)
        print("☕", numbers)
        memory.add_to_memory(numbers[-1])
        print("🔗 Saved value", memory.get_memory())
