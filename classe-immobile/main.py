from immobile import Immobile


class Menu:
    def __init__(self) -> None:

        self.__define_immobile()

    def __define_immobile(self) -> None:
        # Codice, Estensione, Costo, Percentaule
        try:
            codice = self.__input_str(
                "Insersci il codice dell immobile: ",
                "Hai inserito un codice non valido",
            )
            estensione = self.__input_float(
                "Insersci il l'estensione dell immobile in metri quadri: ",
                "Hai inserito una estensione non valida",
                only_positive=True,
            )
            costo = self.__input_float(
                "Insersci il costo dell immobile in euro: ",
                "Hai inserito un costo non valido",
                only_positive=True,
            )
            percentuale = self.__input_int(
                "Insersci la percentuale di tasso del immobile: ",
                "Hai inserito una percentuale di tasso non valida",
                only_positive=True,
            )

            immobile = Immobile(codice, estensione, costo, percentuale)
        except ValueError as e:
            print(e)

    def __input_str(self, input_label: str, error_message: str) -> str:
        valid = False
        while not valid:
            try:
                data = input(f"⚪ {input_label}")
                valid = True
            except ValueError:
                print("❌", error_message)

        return data

    def __input_int(
        self,
        input_label: str,
        error_message: str,
        only_positive=False,
    ) -> int:
        valid = False
        while not valid:
            custom_error = False
            try:
                data = int(input(f"⚪ {input_label}"))
                if only_positive and data < 0:
                    custom_error = True
                    raise ValueError("Devi inserire un numero maggiore o uguale a zero")
                valid = True
            except ValueError as err:
                if custom_error:
                    print("❌", err)
                else:
                    print("❌", error_message)

        return data

    def __input_float(
        self,
        input_label: str,
        error_message: str,
        only_positive=False,
    ) -> float:
        valid = False
        while not valid:
            custom_error = False
            try:
                data = float(input(f"⚪ {input_label}"))
                if only_positive and data < 0:
                    custom_error = True
                    raise ValueError("Devi inserire un numero maggiore o uguale a zero")
                valid = True
            except ValueError as err:
                if custom_error:
                    print("❌", err)
                else:
                    print("❌", error_message)

        return data


if __name__ == "__main__":
    Menu()
