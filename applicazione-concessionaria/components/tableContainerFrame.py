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
        self.configure(fg_color="transparent", height=600, border_width=-6)
        
        self.__define_property()

        filtered_veicoli = self.__get_combobox_value()
        self.__get_veicoli_and_load(filtered_veicoli)
        self.__combobox_binding()
        self.__bind_search_bar()
    
    def __define_property(self):
        self.rows = []

    
    def __get_veicoli_and_load(self, choiche: str):
        # Sto entrando dentro tanti master perché il componente che estende questa classe e a sua volta fatto da diversi altri componenti estesi
        print("🌟", choiche)

        # Prendiamo i rispettivi veicoli controllando il valore nella combobox
        veicoli = self.__get_veicoli(choiche=choiche)        
        self.__load_rows(veicoli)


    def __get_veicoli(self, choiche: str) -> List[Veicolo]:
        veicoli = self.master.master.master.master.get_concessionaria().get_veicoli()
        if choiche.lower() == "Auto Veicoli".lower():
            veicoli = self.master.master.master.master.get_concessionaria().get_autoveicolo()
        elif choiche.lower() == "Auto Carri".lower():
            veicoli = self.master.master.master.master.get_concessionaria().get_autocarro()
        elif choiche.lower() == "Moto Veicoli".lower():
            veicoli = self.master.master.master.master.get_concessionaria().get_motoveicolo()

        return veicoli
    
    def __get_combobox_value(self) -> str:
        combo_box = self.master.master.master.components["client_search_row"].search_combobox
        filtered_veicoli = combo_box.get()

        return filtered_veicoli
    
    # Carica le righe nella tabella, data una lista di Veicoli
    def __load_rows(self, veicoli: List[Veicolo]):
        # Rimuoviamo le righe precedentemente caricate
        self.__ungrid_rows()

        number_of_veicles = len(veicoli)
        self.__update_number_of_veicles(number_of_veicles)
        
        for i, veicolo in enumerate(veicoli):
            # Prediamo i dati dalla classe
            targa = veicolo.get_targa()
            marca = veicolo.get_marca()
            modello = veicolo.get_modello()
            n_posti = veicolo.get_numero_posti()
            prezzo_base = veicolo._get_prezzo_base()
            prezzo = veicolo.get_prezzo()

            # Prediamo il dato specifico
            if isinstance(veicolo, Autoveicolo):
                valore_specifico = f"N° Porte: {veicolo.get_numero_porte()}"
            elif isinstance(veicolo, Autocarro): 
                valore_specifico = f"Capacità massima: {veicolo.get_max_capacity()} Q"
            elif isinstance(veicolo, Motoveicolo):
                valore_specifico = f"Cilindrata: {veicolo.get_cilindrata()} cm³"
            
            if not valore_specifico:
                raise ValueError("la proprietà specifica per per il veicolo non è specificata. Sicuro di stare passando un Veicolo?")
            
            # Creiamo un oggetto per modellizzare i dati da inserire nella tabella
            row_data = RowTableData(model=modello, price=prezzo, nameplate=targa, brand=marca, number_seats=n_posti, base=prezzo_base, other=valore_specifico)
            
            
            # Container per la riga
            row_frame = ctk.CTkFrame(master=self, fg_color="#33333A", height=60)
            row_frame.grid(row=i, pady=(25, 0))
            self.rows.append(row_frame)
            
            # row = TableRow(master=self, data=row_data)
            # row.grid(row=i, column=0, sticky="nsew", pady=(25, 0))
            # Creiamo una riga            
            row = TableRow(master=row_frame, data=row_data)
            row.place(x=5, y=0)

    def __combobox_binding(self):
        self.combo_box = self.master.master.master.components["client_search_row"].search_combobox
        self.combo_box.configure(command=self.__get_veicoli_and_load)
        # self.combo_box.bind("<<ComboboxSelected>>", lambda event: self.get_veicoli_and_load())

    def __ungrid_rows(self):
        for row in self.rows:
            row.grid_forget()

    def __update_number_of_veicles(self, length_list: int):
        number_veicle_frame = self.master.master.master.components["number_of_veicle"]
        number_veicle_frame.update_number(length_list)

    def __search_by_nameplate(self, query: str):
        combobox_value = self.__get_combobox_value()
        veicoli = self.__get_veicoli(combobox_value)

        filtered_veicoli = []
        for veicolo in veicoli:
            match = veicolo.get_targa().startswith(query)
            if match:
                filtered_veicoli.append(veicolo)
        
        self.__load_rows(filtered_veicoli)


    def __bind_search_bar(self):
        search_entry = self.master.master.master.components["client_search_row"].search_entry
        search_entry.bind("<KeyRelease>", lambda event: self.__search_by_nameplate(search_entry.get().upper()))