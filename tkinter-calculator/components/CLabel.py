import tkinter as tk
from tkinter import ttk


class CLabel(ttk.Label):
    def __init__(self, master, **kwargs):
        self.value = tk.StringVar()

        # Impostando una textvariable, il testo del widget verrà aggiornato automaticamente quando il valore della variabile cambia
        # Ma il parametro text verrà ignorato
        super().__init__(
            master=master, textvariable=self.value, **kwargs
        )

        # Impostaiamo la textvariable con il valore passato come parametro
        self.value.set(kwargs.get("text", ""))
