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
            style="Display.TLabel",
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
            "Display.TLabel",
            background="#1D1D1D",
            foreground="#FFFFFF",
            font=("Arial", 30),
        )

    def add_text(self, text):
        current_text = self.display.value.get()
        if current_text == "0":
            self.display.value.set(text)
        else:
            self.display.value.set(current_text + text)
