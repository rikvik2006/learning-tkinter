class App:
    def __init__(self) -> None:
        pass

    def __define_immobile(self) -> None:
        # Codice, Estensione, Costo, Percentaule
        try:
            pass
        except:
            pass

    def __input_data(self, input_label: str, error_message: str) -> str:
        is_valid = False
        while not is_valid:
            try:
                data = input(input_label)
                is_valid = True
            except ValueError:
                print("❌", error_message)

        return data
