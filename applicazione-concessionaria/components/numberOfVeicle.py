import customtkinter as ctk

class NumberOfVeicle(ctk.CTkFrame):
    """Rappresent the frame that cotain the number of veicle"""
    
    def __init__(self, master, layout, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(**layout, pady=(37, 0))
        self.configure(fg_color="transparent")
        self.__load_text()

    def __load_text(self):
        self.text = ctk.CTkLabel(self, text="Numero #: 0",  width=200, height=40, fg_color="#33333A", text_color="#7B7B80", corner_radius=12, justify="left", font=("Segoe UI Semibold", 15))
        self.text.grid(row=0, column=0)

    def update_number(self, number: int) -> None: 
        self.text.configure(text=f"Numero #: {number}")
