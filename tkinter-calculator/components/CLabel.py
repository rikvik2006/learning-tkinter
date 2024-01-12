import tkinter as tk
from tkinter import ttk


class CLabel(ttk.Label):
    def __init__(self, master, text: str, padding: tuple[int, int] = (0, 0)):
        self.value = tk.StringVar()

        # Impostando una textvariable, il testo del widget verrà aggiornato automaticamente quando il valore della variabile cambia
        # Ma il parametro text verrà ignorato
        super().__init__(
            master=master, text=text, textvariable=self.value, padding=padding
        )

        # Impostaiamo la textvariable con il valore passato come parametro
        self.value.set(text)
