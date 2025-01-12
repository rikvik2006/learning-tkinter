import customtkinter as ctk

class OperatorTabFrame(ctk.CTkFrame):
    """Frame shown when the operator tab is selected"""

    def __init__(self, master, layout, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(**kwargs)
        self.configure(fg_color="transparent")

        self.label = ctk.CTkLabel(self, text="Cooming soon", font=("Segoe UI Semibold", 17))
        self.label.grid(column=0, row=0, sticky="nsew")