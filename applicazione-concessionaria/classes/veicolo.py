from abc import ABC, abstractmethod


class Veicolo(ABC):
    """Rappresnta un vicolo generico"""

    def __init__(
        self,
        targa: str,
        marca: str,
        modello: str,
        n_posti: int,
        prezzo_base: float,
    ) -> None:
        self.set_targa(targa)
        self.set_marca(marca)
        self.set_modello(modello)
        self.set_numero_posti(n_posti)
        self._set_prezzo_base(prezzo_base)

    def __str__(self) -> str:
        return f"""\
Marca: {self.__marca} - Modello: {self.__modello} - Prezzo: {self.get_prezzo()}"""

    def set_targa(self, targa: str) -> None:
        self.__targa = targa

    def set_marca(self, marca: str) -> None:
        self.__marca = marca

    def set_modello(self, modello: str) -> None:
        self.__modello = modello

    def set_numero_posti(self, n_posti: int) -> None:
        if n_posti <= 0:
            raise ValueError(
                "devi inserire un numero di posti maggiore di zero"
            )
        self.__n_posti = n_posti

    def _set_prezzo_base(self, prezzo_base: float) -> None:
        if prezzo_base <= 0:
            raise ValueError(
                "il prezzo di base del veicolo deve essere maggiore di zero"
            )
        self.__prezzo_base = prezzo_base

    def get_targa(self) -> str:
        return self.__targa

    def get_marca(self) -> str:
        return self.__marca

    def get_modello(self) -> str:
        return self.__modello

    def get_numero_posti(self) -> int:
        return self.__n_posti

    def _get_prezzo_base(self) -> float:
        return self.__prezzo_base

    @abstractmethod
    def get_prezzo(self) -> float:
        pass
