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
