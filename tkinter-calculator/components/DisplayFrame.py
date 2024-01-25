from tkinter import ttk
from components.CLabel import CLabel


class DisplayFrame(ttk.Frame):
    def __init__(self, master, layout, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(**layout)
        self.create_display()
        self.display.value.set("0")

    def create_display(self):
        self.display = CLabel(
            master=self,
            text="0",
            anchor="ne",
            style="Display.TLabel",
        )
        self.display.grid(row=0, column=0, sticky="nsew")

    def add_text(self, text):
        current_text = self.display.value.get()
        if current_text == "0":
            self.display.value.set(text)
        else:
            self.display.value.set(current_text + text)
