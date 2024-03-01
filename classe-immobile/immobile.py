class Immobile:
    """Rappresenta un errore"""

    def __init__(
        self,
        codice: str,
        estensione: float,
        costo_m_quadro: float,
        percentuale: float,
    ) -> None:
        self.inserisci(codice, estensione, costo_m_quadro, percentuale)

    def __str__(self) -> str:
        return f"""
        -----------------------------
        🏠 Immobile:
            Codice: {self.__codice}
            Estensione: {self.__estensione}
            Costo Metro Quadro: {self.__costo_metro_quadro}
            Percentaule di tasso: {self.__percentuale_tasse}
        -----------------------------
        """

    def set_codice(self, codice: str) -> None:
        self.__codice = codice

    def set_estensione(self, estensione: float) -> None:
        self.__estensione = estensione

    def set_costo_metro_quadro(self, costo_m_quadro: float) -> None:
        self.__costo_metro_quadro = costo_m_quadro

    def set_percentuale_tasse(self, percentuale: float) -> None:
        self.__percentuale_tasse = percentuale

    def get_codice(self) -> str:
        return self.__codice

    def get_estensione(self) -> float:
        return self.__estensione

    def get_costo_metro_quadro(self) -> float:
        return self.__costo_metro_quadro

    def get_percentuale_tasse(self) -> float:
        return self.__percentuale_tasse

    def inserisci(
        self, codice: str, estensione: float, costo_m_quadro: float, percentuale: float
    ) -> None:
        self.set_codice(codice)
        self.set_estensione(estensione)
        self.set_costo_metro_quadro(costo_m_quadro)
        self.set_percentuale_tasse(percentuale)

    def calcola_valore(self) -> float:
        valore_immobile = self.get_costo_metro_quadro() * self.get_estensione()
        return valore_immobile

    def calcola_tassa(self) -> float:
        tassa_in_percentaule = (
            self.calcola_valore() * self.get_percentuale_tasse() / 100
        )

        return tassa_in_percentaule

    def calcola_valore_totale(self):
        valore_totale = self.calcola_valore() + self.calcola_tassa()
        return valore_totale
