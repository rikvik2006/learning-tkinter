import tkinter as tk
from typing import Tuple
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        ctk.set_appearance_mode("dark")


if __name__ == "__main__":
    app = App()
    app.mainloop()
