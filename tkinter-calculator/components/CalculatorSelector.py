from tkinter import ttk
import tkinter as tk


class CalculatorSelector(ttk.LabelFrame):
    def __init__(self, master, layout, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.grid(**layout)
        self["text"] = "Selettore calcolatrice"
        self.__create_radio_buttons()

    def __create_radio_buttons(self):
        self.__selected_value = tk.IntVar()
        ttk.Radiobutton(
            self,
            text="Standard",
            value=0,
            variable=self.__selected_value,
            command=self.chnage_frame,
        ).grid(row=0, column=0)
        ttk.Radiobutton(
            self,
            text="Scientifica",
            value=1,
            variable=self.__selected_value,
            command=self.chnage_frame,
        ).grid(row=0, column=1)

        self.__selected_value.set(0)

    def get_selected_value(self):
        return self.__selected_value.get()

    def set_selected_value(self, value):
        self.__selected_value.set(value)

    def chnage_frame(self):
        frame = self.master.calculator[self.get_selected_value()]
        frame.tkraise()
