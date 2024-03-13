import tkinter as tk
from typing import Tuple
import customtkinter as ctk
from components.loadComponents import LoadComponents


class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        ctk.set_appearance_mode("dark")
        self.configure(fg_color="#282830")
        LoadComponents().loads(master=self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
