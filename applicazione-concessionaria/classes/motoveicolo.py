from classes.veicolo import Veicolo


class Motoveicolo(Veicolo):
    """Rappresenta un motoveicolo"""

    def __init__(
        self,
        targa: str,
        marca: str,
        modello: str,
        n_posti: int,
        prezzo_base: float,
        cilindrata: int,
    ) -> None:
        super().__init__(targa, marca, modello, n_posti, prezzo_base)
        self.set_cilindrata(cilindrata)

    def __str__(self) -> str:
        return f"{super().__str__()} - Cilindrata: {self.__cilindrata}"

    def set_cilindrata(self, cilindrata: int) -> None:
        if cilindrata <= 0:
            raise ValueError(
                "devi inserire una cilindrata maggiore di zero per il motoveicolo"
            )

        self.__cilindrata = cilindrata

    def get_cilindrata(self) -> int:
        return self.__cilindrata

    def get_prezzo(self) -> float:
        return self._get_prezzo_base() * self.__cilindrata
