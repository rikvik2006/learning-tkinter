from typing import List, Dict
from turtle import heading
import customtkinter as ctk
from components.styledHeaderLabel import StyledHeaderLabel 


class TableHeaderFrame(ctk.CTkFrame):
    """Rappresent the table header in client tab"""

    def __init__(self, master, layout, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(**layout, pady=(25, 0))
        # self.configure(fg_color="#9BB0C1")
        self.configure(fg_color="#33333A")
        self.__load_columns()
        
    def __load_columns(self):
        self.grid_template_columns = [
            {
                "text": "#",
                "padx": (20, 0)
            },
            {
                "text": "Modello",
                "padx": (40, 0)
            },
            {
                "text": "Prezzo",
                "padx": (100, 0)
            },
            {
                "text": "Targa",
                "padx": (200, 0)
            },
            {
                "text": "Marca",
                "padx": (100, 0)
            },
            {
                "text": "Numero Posti",
                "padx": (100, 0)
            },
            {
                "text": "Prezzo Base",
                "padx": (100, 0)
            },
            {
                "text": "Altro",
                "padx": (100, 20)
            },
            
        ]

        self.columns = []

        for i, column in enumerate(self.grid_template_columns):
            text = column["text"]
            padx = column["padx"]

            new_column = StyledHeaderLabel(self, text=text)
            new_column.grid(row=0, column=i, padx=padx) 
            self.columns.append(new_column)
        
    def get_header_labels_x_position(self) -> List[int]:
        relative_postion = []
        for column_label in self.columns:
            relative_postion.append(column_label.winfo_x())
        
        return relative_postion
    
    def get_grid_template_column(self) -> List[Dict]:
        return self.grid_template_columns