from typing import List
from classes.dolce import Dolce

class Torta(Dolce):
    @property
    def _ALLERGENI(self) -> List[str]:
        return  ["uovo", "latte", "zucchero"]
    
    def __init__(self, 
        nome: str, 
        descrizione: str, 
        peso: int, 
        prezzo: float, 
        ingredienti: List[str],
        temp_conservazione: float
    ) -> None:
        super().__init__(nome, descrizione, peso, prezzo, ingredienti)
        self.set_temp_conservazione(temp_conservazione)
        
    def __str__(self) -> str:
        return f"""{super().__str__()}
"""
    
    def set_temp_conservazione(self, temp: float) -> None:
        if not isinstance(temp, float):
            raise TypeError("la temperatura deve essere di tipo float")
        
        self.__temp_conservazione = temp

    def get_temp_conservazione(self) -> float:
        return self.__temp_conservazione
        

    