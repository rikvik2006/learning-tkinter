import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        label = ttk.Label(self, text="test")
        label.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()