from immobile import Immobile


class Garage(Immobile):
    """Rappresenta un garage"""

    def __init__(
        self,
        codice: str,
        estensione: float,
        costo_m_quadro: float,
        percentuale: float,
        interrato: bool,
    ) -> None:
        super().__init__(codice, estensione, costo_m_quadro, percentuale)
        self.set_interato(interrato)

    def __str__(self) -> str:
        old_str = super().__str__()
        old_str.replace("Immobile", "Garage")
        old_str.replace("-----------------------------", "")

        new_str = f"""{old_str}
            È interato: {self.__interrato}
            -----------------------------
        """

        return new_str

    def set_interato(self, interrato: bool) -> None:
        if not isinstance(interrato, bool):
            raise ValueError("interrato deve essere un booleano")

        self.__interrato = interrato

    def get_interato(self) -> bool:
        return self.__interrato
