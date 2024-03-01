from immobile import Immobile


class Alloggio(Immobile):
    def __init__(
        self,
        codice: str,
        estensione: float,
        costo_m_quadro: float,
        percentuale: float,
        numero_stanze: int,
    ) -> None:
        super().__init__(codice, estensione, costo_m_quadro, percentuale)

        self.set_numero_stanze(numero_stanze)

    def __str__(self) -> str:
        old_str = super().__str__()
        old_str.replace("Immobile", "Alloggio")
        old_str.replace("-----------------------------", "")

        new_str = f"""{old_str}
            Numero di stanze: {self.__numero_stanze}
            -----------------------------
        """

        return new_str

    def set_numero_stanze(self, numero_stanze: int) -> None:
        if not isinstance(numero_stanze, int):
            raise ValueError("il numero di stanze deve essere un intero")

        if numero_stanze <= 0:
            raise ValueError("il numero di stanze deve essere maggiore di zero")

        self.__numero_stanze = numero_stanze

    def get_numero_stanze(self) -> int:
        return self.__numero_stanze
