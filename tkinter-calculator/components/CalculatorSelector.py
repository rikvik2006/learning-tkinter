from tkinter import ttk
import tkinter as tk


class CalculatorSelector(ttk.LabelFrame):
    def __init__(self, master, layout, **kwargs) -> None:
        super().__init__(master, style="Calculator.TLabelframe")
        self.grid(**layout)
        self["text"] = "Selettore calcolatrice"

        self.__create_radio_buttons()
        self.__create_style()

    def __create_radio_buttons(self):
        self.__selected_value = tk.IntVar()
        self.radio1 = ttk.Radiobutton(
            self,
            text="Standard",
            value=0,
            variable=self.__selected_value,
            command=self.chnage_frame,
            style="Calculator.TRadiobutton",
        ).grid(row=0, column=0)
        self.radio2 = ttk.Radiobutton(
            self,
            text="Scientifica",
            value=1,
            variable=self.__selected_value,
            command=self.chnage_frame,
            style="Calculator.TRadiobutton",
        ).grid(row=0, column=1)

        self.__selected_value.set(0)

    def __create_style(self):
        self.style = ttk.Style()
        self.style.configure(
            "Calculator.TRadiobutton",
            background="#1D1D1D",
            foreground="white",
            activebackground="#1D1D1D",
        )
        self.style.configure("Calculator.TLabelframe", background="#1D1D1D")

    def get_selected_value(self):
        return self.__selected_value.get()

    def set_selected_value(self, value):
        self.__selected_value.set(value)

    def chnage_frame(self):
        frame = self.master.calculator[self.get_selected_value()]
        frame.tkraise()
