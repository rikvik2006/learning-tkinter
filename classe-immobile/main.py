from immobile import Immobile
import tkinter
from tkinter import ttk
from components.CEntry import CEntry
from components.CLabel import CLabel


class App(tkinter.Tk):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.title("Registra Immobili")
        self.create_input_frame()
        self.create_console()

    def create_input_frame(self) -> None:
        self.input_frame = ttk.Frame(self)
        self.input_frame.grid(row=0, column=0, sticky="e")
        self.input_frame["padding"] = (10, 10, 10, 10)
        self.input_frame["relief"] = "groove"

        self.input_layout = [
            [CLabel(self.input_frame, text="Codice"), CEntry(self.input_frame), (1, 1)],
            [
                CLabel(self.input_frame, text="Estensione"),
                CEntry(self.input_frame),
                (3, 1),
            ],
            [
                CLabel(self.input_frame, text="Costo al metro quadro"),
                CEntry(self.input_frame),
                (5, 1),
            ],
            [
                CLabel(self.input_frame, text="Percentuale"),
                CEntry(self.input_frame),
                (7, 1),
            ],
            [ttk.Button(self.input_frame, text="Inserisci"), (9, 1)],
        ]

        for i, row in enumerate(self.input_layout):
            for i, pack in enumerate(self.input_layout):
                if len(pack) != 2:
                    label = pack[0]
                    entry = pack[1]
                    position = pack[2]

                    label.grid(row=position[0], column=position[1])
                    entry.grid(row=position[0] + 1, column=position[1])
                else:
                    button = pack[0]
                    position = pack[1]

                    button["padding"] = (5, 0, 5, 0)
                    button.grid(row=position[0], column=position[1])

        # self.codice_entry.grid(row=1, column=1, sticky="ne")

    def create_utilis_frame(self):
        self.utils_frame = ttk.Frame(self)
        self.utils_frame.grid(row=1, column=2)

    def create_console(self):
        self.console_frame = ttk.Frame(self)
        self.console_frame.grid(row=1, column=0)

        self.console = CLabel(self.console_frame, text="Oggetto Oggetto")
        self.console["padding"] = 7
        self.console["relief"] = "groove"
        self.console.grid(row=0, column=0)
        self.console["height"] = 100


if __name__ == "__main__":
    app = App()
    app.mainloop()
