from cgitb import text
from turtle import width
import customtkinter as ctk

from components.styledHeaderLabel import StyledHeaderLabel
from utils.types import RowTableData


class TableRow(ctk.CTkFrame):
    """Rappresent a table row inside the table in the client tab"""

    def __init__(self, master, data: RowTableData, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(fg_color="transparent", height=60)
        self.__load_data(data)
        

    def __load_data(self, data: RowTableData):
        data_dict = data()
        self.data_columns = []
        
        table_header_frame = self.master.master.master.master.master.components["table_header_frame"]
        # Prediamo la posizione relativa in pixel delle colonne nel header, in modo tale da posizionare i valori allineati
        column_relative_position = table_header_frame.get_header_labels_x_position()

        
        for i, data_column in enumerate(data_dict):
            value = data_column["value"]
            padx = data_column["padx"]

            if i == 0:
                # Renderizziamo l'immagine
                new_data = StyledHeaderLabel(self, image=value, text="", height=60)
                # new_data.grid(row=0, column=i, padx=padx)
                # place_y = ((10 + 60) * i)
                new_data.place(x=column_relative_position[i], y=0)
            else:
                # Renderiziamo i dati                
                new_data = StyledHeaderLabel(self, text=value, height=60)
                # new_data.grid(row=0, column=i, padx=padx)
                # place_y = ((10 + 60) * i)
                new_data.place(x=column_relative_position[i], y=0)

            new_data.update_idletasks()
            self.data_columns.append(new_data)
        
        # Calcoliamo la grandezza del nostro Frame, e di quello padre, dato che utilizzando il metodo place per posizione gli elementi perdiamo la grandezza dinamica
        last_widget_width = self.data_columns[-1].winfo_width()
        last_widget_padx_right = data_dict[-1]["padx"][1]
        last_widget_position = column_relative_position[-1]
        table_row_total_width = last_widget_width + last_widget_position + last_widget_padx_right
        self.configure(width=table_row_total_width)
        self.master.configure(width=1358)
        
