from msilib import Table
from multiprocessing import Value
import customtkinter as ctk
from typing import List

from classes.veicolo import Veicolo
from classes.autoveicolo import Autoveicolo
from classes.autocarro import Autocarro 
from classes.motoveicolo import Motoveicolo

from utils.types import RowTableData
from components.tableRow import TableRow

class TableContainerFrame(ctk.CTkScrollableFrame):
    """Rappresent the container of the table in client tab"""

    def __init__(self, master, layout, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(**layout)
        # pady=(25, 0)
        veicoli = self.master.master.master.master.get_concessionaria().get_veicoli()
        self.configure(fg_color="transparent", height=600, border_width=-6)
        self.__load_rows(veicoli)
        
    def __load_rows(self, veicoli: List[Veicolo]):
        self.rows = []

        for i, veicolo in enumerate(veicoli):
            targa = veicolo.get_targa()
            marca = veicolo.get_marca()
            modello = veicolo.get_modello()
            n_posti = veicolo.get_numero_posti()
            prezzo_base = veicolo._get_prezzo_base()
            prezzo = veicolo.get_prezzo()

            # TODO: Prendere la proprietà speciale per i tipi di veicoli controllando il tipo dell instanza (isinstance)
            if isinstance(veicolo, Autoveicolo):
                valore_specifico = veicolo.get_numero_porte()
            elif isinstance(veicolo, Autocarro): 
                valore_specifico = veicolo.get_max_capacity()
            elif isinstance(veicolo, Motoveicolo):
                valore_specifico = veicolo.get_cilindrata()
            
            if not valore_specifico:
                raise ValueError("la proprietà specifica per per il veicolo non è specificata. Sicuro di stare passando un Veicolo?")

            row_data = RowTableData(model=modello, price=prezzo, nameplate=targa, brand=marca, number_seats=n_posti, base=prezzo_base, other=valore_specifico)

            row_frame = ctk.CTkFrame(master=self, fg_color="#33333A", height=60)
            row_frame.grid(row=i, pady=(25, 0))

            # row = TableRow(master=self, data=row_data)
            # row.grid(row=i, column=0, sticky="nsew", pady=(25, 0))
            row = TableRow(master=row_frame, data=row_data)
            row.place(x=5, y=0)