import customtkinter as ctk

class ClientTabFrame(ctk.CTkFrame):
    """Frame shown when the client tab is selected"""

    def __init__(self, master, layout, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(**layout, pady=(37, 0))
        self.configure(fg_color="red")