from tkinter import ttk
from components.Display import Display
from components.CLabel import CLabel


# TODO: Creare una superclasse Display che gestisca l'ho stile, la grandezza, e la poszione del display
class InfoDisplayFrame(ttk.Frame):
    def __init__(self, master, layout, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(**layout)
        self.create_display()
        self.create_style()
        self.display.value.set("M")

    def create_display(self):
        self.display = CLabel(
            master=self,
            text="0",
            anchor="nw",
            style="InfoDisplay.TLabel",
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
            "InfoDisplay.TLabel",
            background="#1D1D1D",
            foreground="#FFFFFF",
            font=("Arial", 15),
        )
