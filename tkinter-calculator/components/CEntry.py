import tkinter as tk
from tkinter import ttk


class CEntry(ttk.Entry):
    def __init__(self, master):
        self.value = tk.StringVar()

        super().__init__(master=master, textvariable=self.value)