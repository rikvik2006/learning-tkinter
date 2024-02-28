from typing import Union
from immobile import Immobile


class Agenzia:
    """Rappresenta una agenzia immobiliare"""

    def __init__(self) -> None:
        self.__immobili: list[Immobile] = []

    def get_immobili(self) -> list[Immobile]:
        return self.__immobili

    def set_immobili(self, immobili: list[Immobile]) -> None:
        for immobile in immobili:
            if not isinstance(immobile, Immobile):
                raise TypeError("la lista immobli deve contenere Immobili")

        self.__immobili = immobili

    def get_immobile(self, codice: str) -> list[Immobile]:
        if not isinstance(codice, str):
            raise ValueError("il codice deve essere una stringa")

        found_immobili = []
        for immobile in self.__immobili:
            if immobile.get_codice() == codice:
                found_immobili.append(immobile)

        return found_immobili

    def get_immobile_by_price(
        self, low_range: float, high_range: float
    ) -> list[Immobile]:
        found_immobili: list[Immobile] = []
        for immobile in self.__immobili:
            if low_range <= immobile.calcola_valore() <= high_range:
                found_immobili.append(immobile)

        return found_immobili

    def get_immobile_by_max_extension(self) -> list[Immobile]:
        immobili_estensione = [
            immobile.get_estensione() for immobile in self.__immobili
        ]
        found_immobili: list[Immobile] = [
            immobile
            for immobile in self.__immobili
            if immobile.get_estensione() == max(immobili_estensione)
        ]

        return found_immobili

    def calculate_mean_tax(self) -> float:
        tax_sum = 0
        for immobile in self.__immobili:
            tax_sum += immobile.get_percentuale_tasse()

        mean_tax = tax_sum / len(self.__immobili)
        return mean_tax
