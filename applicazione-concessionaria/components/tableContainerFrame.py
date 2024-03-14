from msilib import Table
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
        self.configure(fg_color="#EEA5A6")
        self.__load_rows()
        
    def __load_rows(self, veicoli: List[Veicolo]):
        self.rows = []

        # veicoli = self.master.master.master.master.get_concessionaria().get_veicoli()
        # print("💀",  veicoli)
        for veicolo in veicoli:
            targa = veicolo.get_targa()
            marca = veicolo.get_marca()
            modello = veicolo.get_modello()
            n_posti = veicolo.get_numero_posti()
            prezzo_base = veicolo._get_prezzo_base()
            prezzo = veicolo.get_prezzo()

            # TODO: Prendere la proprietà speciale per i tipi di veicoli controllando il tipo dell instanza (isinstance)

            data = RowTableData(model=modello, price=prezzo, nameplate=targa, brand=marca, number_seats=n_posti, base=prezzo_base, other=)
            new_row = TableRow()