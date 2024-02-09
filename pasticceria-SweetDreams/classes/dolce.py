from abc import ABC, abstractmethod
from typing import List, Dict

class Dolce(ABC):
    def __init__(self, nome: str, descrizione: str, peso: int, prezzo: float, ingredienti: List[str]) -> None:
        self.set_nome(nome)
        self.set_descrizione(descrizione)
        self.set_peso(peso)
        self.set_prezzo(prezzo)
        self.set_ingredienti(*ingredienti)

    def __str__(self) -> str:
        return f"""
Nome: {self.__nome}
Descrizione: {self.__descrzione}
Peso: {self.__peso}
Prezzo: {self.__prezzo}
Ingredienti: {",".join(self.__ingredienti)}
"""

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def set_descrizione(self, descrizione: str) -> None:
        self.__descrzione = descrizione

    def set_peso(self, peso: int) -> None:
        # Peso in grammi
        self.__peso = peso

    def set_prezzo(self, prezzo: float) -> None:
        self.__prezzo = prezzo

    def set_ingredienti(self, *ingredienti: str) -> None:
        for ingrediente in ingredienti:
            if not isinstance(ingrediente, str):
                raise TypeError("gli ingredienti possono essere solo delle stringhe")
        self.__ingredienti: List[str] = list(ingredienti)

    def get_nome(self) -> str:
        return self.__nome
    
    def get_descrizione(self) -> str:
        return self.__descrzione
    
    def get_peso(self) -> int:
        return self.__peso
    
    def get_prezzo(self) -> float: 
        return self.__prezzo
    
    def get_ingredienti(self) -> List[str]:
        return self.__ingredienti
    
    # @abstractmethod
    # def allergeni(self) -> Dict[str, bool]:
    #     pass
    
    @property
    @abstractmethod
    def _ALLERGENI(self) -> List[str]:
        pass

    def get_allergeni(self) -> List[str]:
        return self._ALLERGENI
    
    def allergeni(self) -> Dict[str, bool]:
        ingredienti = self.get_ingredienti()
        for allergeno in self._ALLERGENI: 
            allergeni: Dict[str, bool] = {} 
            allergeni[allergeno] = False
        for ingrediente in ingredienti:
            if ingrediente in self._ALLERGENI:
                allergeni[ingrediente] = True

        return allergeni