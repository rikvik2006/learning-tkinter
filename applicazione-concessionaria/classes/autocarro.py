from classes.veicolo import Veicolo


class Autocarro(Veicolo):
    """Rappresenta un autocarro"""

    def __init__(
        self,
        targa: str,
        marca: str,
        modello: str,
        n_posti: int,
        prezzo_base: float,
        max_capacity: int,
    ) -> None:
        super().__init__(targa, marca, modello, n_posti, prezzo_base)
        self.set_max_capacity(max_capacity)

    def __str__(self) -> str:
        return f"{super().__str__()} - Capacità massima: {self.__max_capacity}"

    def set_max_capacity(self, max_capacity: int) -> None:
        if max_capacity <= 0:
            raise ValueError(
                "la capacità massima dell auto carro deve essere maggiore di zero"
            )

        self.__max_capacity = max_capacity

    def get_max_capacity(self) -> int:
        return self.__max_capacity

    def get_prezzo(self) -> float:
        return self._get_prezzo_base() * self.__max_capacity
