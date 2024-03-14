from turtle import mode
from typing import List

from classes.autocarro import Autocarro
from classes.autoveicolo import Autoveicolo
from classes.motoveicolo import Motoveicolo
from classes.veicolo import Veicolo


class Concessionaria:
    """Rappresenta una concessionaria"""

    def __init__(self) -> None:
        self.__veicoli: List[Veicolo] = []

    def set_veicoli(self, veicoli: List[Veicolo]) -> None:
        for veicolo in veicoli:
            if not isinstance(veicolo, Veicolo):
                raise ValueError(
                    "devi inserire una lista contente solo oggetti di tipo Veicolo"
                )
        self.__veicoli = veicoli

    def get_veicoli(self) -> List[Veicolo]:
        return self.__veicoli

    def get_autoveicolo(self) -> List[Autoveicolo]:
        return [
            veicolo
            for veicolo in self.__veicoli
            if isinstance(veicolo, Autoveicolo)
        ]

    def get_autocarro(self) -> List[Autocarro]:
        return [
            veicolo
            for veicolo in self.__veicoli
            if isinstance(veicolo, Autocarro)
        ]

    def get_motoveicolo(self) -> List[Motoveicolo]:
        return [
            veicolo
            for veicolo in self.__veicoli
            if isinstance(veicolo, Motoveicolo)
        ]
    
    # TODO: Aggiungere controlli di tipo
    def add_autoveicolo(
            self,
            targa: str,
            marca: str,
            modello: str,
            n_posti: int,
            prezzo_base: float,
            numero_porte: int
    ) -> None:
        autoveicolo = Autoveicolo(targa, marca, modello, n_posti, prezzo_base, numero_porte)
        self.__veicoli.append(autoveicolo)
        
    def add_autocarro(
            self,
            targa: str,
            marca: str,
            modello: str,
            n_posti: int,
            prezzo_base: float,
            max_capacity: int
    ) -> None:
        autocarro = Autocarro(targa, marca, modello, n_posti, prezzo_base, max_capacity)
        self.__veicoli.append(autocarro)

    def add_motoveicolo(
            self,
            targa: str,
            marca: str,
            modello: str,
            n_posti: int,
            prezzo_base: float,
            cilindrata: int
    ) -> None:
        motoveicolo = Motoveicolo(targa, marca, modello, n_posti, prezzo_base, cilindrata)
        self.__veicoli.append(motoveicolo)