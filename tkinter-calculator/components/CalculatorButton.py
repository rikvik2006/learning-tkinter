from tkinter import ttk
import tkinter as tk


class CalculatorButton(ttk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Add some style
        self.style = ttk.Style()
        # self.style.theme_use("alt")
        # self.style.configure("CalculatorButton.TButton", font=("Helvetica", 16), background="#3B3B3B", foreground="white", )
        # self.configure(style="CalculatorButton.TButton")
        # self.style.map("CalculatorButton.TButton", background=[("active", "#313331")])
        self.configure_style()

    def configure_style(self):
        # Configurazione dello stile predefinito
        self.style.configure(
            "CalculatorButton.TButton", background="#3B3B3B", foreground="white"
        )

        # Configurazione dello stile al passaggio del mouse
        self.style.map(
            "CalculatorButton.TButton",
            background=[("active", "#313331")],
            foreground=[("active", "white")],
        )

        # Configurazione dello stile al clic del mouse
        self.style.map(
            "CalculatorButton.TButton",
            background=[("pressed", "#212121")],
            foreground=[("pressed", "white")],
        )

        # Applicazione dello stile al bottone
        self.configure(style="CalculatorButton.TButton")
