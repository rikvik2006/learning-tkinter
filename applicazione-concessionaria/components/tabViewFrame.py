import customtkinter as ctk
from components.cbutton import CButton

class TabViewFrame(ctk.CTkFrame):
    def __init__(self, master, layout, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(**layout)
        self.__frames_layout = dict({ 
            "row": 1, 
            "column": 0,
            "sticky": "nsew",
            "pady": (37, 0)
        })
        self.__define_buttons()
        self.__set_style()
    
    def __define_buttons(self):
        self.client_button = CButton(master=self, text="Cliente", command=self.__client_button_command)
        self.operator_button = CButton(master=self, text="Operatore", command=self.__operator_button_command)
        self.client_button.grid(row=0, column=0, padx=(0, 15))
        self.operator_button.grid(row=0, column=1)

    def __set_style(self): 
        self.configure(fg_color="#282830")

    def ungrid_client_frame(self):
        self.master.components["client_tab"].grid_forget()

    def ungrid_operator_frame(self):
        self.master.components["operator_tab"].grid_forget()

    def grid_client_frame(self):
        self.master.components["client_tab"].grid(**self.__frames_layout)

    def grid_operator_frame(self):
        self.master.components["operator_tab"].grid(**self.__frames_layout)

    def __client_button_command(self):
        self.ungrid_operator_frame() 
        self.grid_client_frame()

    def __operator_button_command(self):
        self.ungrid_client_frame()
        self.grid_operator_frame()