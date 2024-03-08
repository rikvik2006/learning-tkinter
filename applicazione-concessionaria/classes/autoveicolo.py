from classes.veicolo import Veicolo


class Autoveicolo(Veicolo):
    """Rappresenta un autoveicolo"""

    def __init__(
        self,
        targa: str,
        marca: str,
        modello: str,
        n_posti: int,
        prezzo_base: float,
        numero_porte: int,
    ) -> None:
        super().__init__(targa, marca, modello, n_posti, prezzo_base)
        self.set_numero_porte(numero_porte)

    def __str__(self) -> str:
        return f"{super().__str__()} - Numero porte: {self.__numero_porte}"

    def set_numero_porte(self, n_porte: int) -> None:
        if n_porte <= 0:
            raise ValueError(
                "il numero di porte del auto veicolo deve essere maggiore di zero"
            )

        self.__numero_porte = n_porte

    def get_numero_porte(self) -> int:
        return self.__numero_porte

    def get_prezzo(self) -> float:
        return self._get_prezzo_base() * self.__numero_porte
