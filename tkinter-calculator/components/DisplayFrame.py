from tkinter import ttk
from components.CLabel import CLabel


class DisplayFrame(ttk.Frame):
    def __init__(self, master, layout, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(**layout)
        self.create_display()
        self.create_style()
        self.display.value.set("0")

    def create_display(self):
        self.display = CLabel(
            master=self,
            text="0",
            anchor="nw",
            style="DisplayFrame.TLabel",
        )
        # Posiziona il widget nella posizione 0,0 del frame
        self.display.grid(
            row=0,
            column=0,
            sticky="nsew",
        )
        self.display.config(width=1)

    def create_style(self):
        # Imposta la grandezza della colonna 0 al 100% della grandezza del frame padre
        self.grid_columnconfigure(0, weight=1)

        self.style = ttk.Style()
        self.style.theme_use("alt")
        self.style.configure(
            "DisplayFrame.TLabel",
            background="#1D1D1D",
            foreground="#FFFFFF",
            font=("Arial", 30),
        )

    # Metodi per la gestione del displayFrame

    # Restituisce il testo attuale del display
    def get_text(self) -> str:
        return self.display.value.get()

    # Imposta il testo del display
    def set_text(self, text: str) -> None:
        if isinstance(text, str):
            self.display.value.set(text)
        else:
            raise TypeError("Text must be a string")

    # Agginge un testo al display
    def add_text(self, text) -> None:
        current_text = self.display.value.get()
        if current_text == "0":
            self.display.value.set(text)
        else:
            self.display.value.set(current_text + text)

    # Elimina il testo attuale del display
    def clear(self) -> None:
        self.display.value.set("0")

    # Cancella l'ultimo caratere dal display
    def backspace(self) -> None:
        current_text = self.display.value.get()
        if len(current_text) > 1:
            self.display.value.set(current_text[:-1])
        else:
            self.display.value.set("0")
