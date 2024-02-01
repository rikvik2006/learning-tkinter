from tkinter import ttk
from components.Display import Display
from components.CLabel import CLabel


# TODO: Creare una superclasse Display che gestisca l'ho stile, la grandezza, e la poszione del display
class InfoDisplayFrame(ttk.Frame):
    def __init__(self, master, layout, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(**layout)
        self.__create_displays()
        self.__create_style()

    def __create_displays(self):
        self.memory_display = CLabel(
            master=self,
            anchor="nw",
            style="InfoDisplay.TLabel",
        )
        # Posiziona il widget nella posizione 0,0 del frame
        self.memory_display.grid(
            row=0,
            column=0,
            sticky="nsew",
        )
        # self.memory_display.config(width=1)
        self.error_display = CLabel(
            master=self,
            anchor="ne",
            style="InfoDisplay.TLabel",
        )
        self.error_display.grid(
            row=0,
            column=1,
            sticky="ne",
            rowspan=2,
        )

    def __create_style(self):
        # Imposta la grandezza della colonna 0 al 100% della grandezza del frame padre
        self.grid_columnconfigure(1, weight=1)

        self.info_style = ttk.Style()
        self.info_style.theme_use("alt")
        self.info_style.configure(
            "InfoDisplay.TLabel",
            background="#1D1D1D",
            foreground="#FFFFFF",
            font=("Arial", 15),
        )

    # Metodi per la gestione del info display

    def set_memory_indicator(self, status: bool) -> None:
        if status:
            self.memory_display.value.set("M")
        else:
            self.memory_display.value.set("")

    def set_err(self, err: str) -> None:
        self.error_display.value.set(err)

    def clear_err(self) -> None:
        self.error_display.value.set("")

    def get_err(self) -> str:
        return self.error_display.value.get()
