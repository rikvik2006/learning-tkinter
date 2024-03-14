from cgitb import text
import customtkinter as ctk

from components.styledHeaderLabel import StyledHeaderLabel
from utils.types import RowTableData


class TableRow(ctk.CTkFrame):
    """Rappresent a table row inside the table in the client tab"""

    def __init__(self, master, data: RowTableData, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(fg_color="#33333A", )
        self.__load_data(data)
        

    def __load_data(self, data: RowTableData):
        data_dict = data()
        self.data_columns = []
        
        image = StyledHeaderLabel(self, text="IMAGE")
        image.grid(row=0, column=0)
        self.data_columns.append(image)
        
        for i, data_column in enumerate(data_dict):
            value = data_column["value"]
            padx = data_column["padx"]

            new_data = StyledHeaderLabel(self, text=value, height="60")
            new_data.grid(row=0, column=i + 1, padx=padx)
        
