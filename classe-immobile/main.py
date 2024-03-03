from immobile import Immobile
from alloggio import Alloggio
from garage import Garage
from agenzia import Agenzia
from typing import Union


class Menu:
    def __init__(self) -> None:
        self.__agenzia = Agenzia()
        self.active = True

        for i in range(3):
            print(f"🏠 Insersci i dati per il {i + 1}° immobile")
            self.__define_immobile()

        while self.active:
            self.__print_menu()
            self.__manage_menu_choiche()

    def __define_immobile(self) -> None:
        # Codice, Estensione, Costo, Percentaule
        try:
            # Può assumere il valore di: alloggio, garage, immobile
            type_immobile = self.__get_immobile_type()
            codice = self.__input_str(
                "Insersci il codice dell immobile: ",
                "Hai inserito un codice non valido",
            )
            estensione = self.__input_float(
                "Insersci il l'estensione dell immobile in metri quadri: ",
                "Hai inserito una estensione non valida",
                only_positive=(True, True),
            )
            costo_m_quadro = self.__input_float(
                "Insersci il costo per metro quadro dell immobile: ",
                "Hai inserito un costo non valido",
                only_positive=(True, True),
            )
            percentuale = self.__input_int(
                "Insersci la percentuale di tasso del immobile: ",
                "Hai inserito una percentuale di tasso non valida",
                only_positive=(True, False),
            )

            if type_immobile == "alloggio":
                type_immobile_params = self.get_type_immobile_params(type_immobile)
                immobile = Alloggio(
                    codice,
                    estensione,
                    costo_m_quadro,
                    percentuale,
                    type_immobile_params,
                )
            elif type_immobile == "garage":
                type_immobile_params = self.get_type_immobile_params(type_immobile)
                immobile = Garage(
                    codice,
                    estensione,
                    costo_m_quadro,
                    percentuale,
                    bool(type_immobile_params),
                )
            elif type_immobile == "immobile":
                immobile = Immobile(codice, estensione, costo_m_quadro, percentuale)

            self.__agenzia.append_immobile(immobile)
        except ValueError as e:
            print(e)

    def __print_menu(self):
        print(
            """
        1. Stampa dati immobile dato il codice
        2. Stampa dati immobile dato un range del valore
        3. Stampa dati immobile massima estensione
        4. Stampa tassa media
        5. Stampa costo totale e estensione dato il codice
        6. Esci
            """
        )

    def __get_immobile_type(self) -> str:
        is_valid = False
        while not is_valid:
            type_immobile = self.__input_str(
                "Insersci il tipo dell immobile: [Alloggio, Garage, Immobile]: ",
                "Insersci una stringa valida",
            )

            if not type_immobile.lower() in ("alloggio", "garage", "immobile"):
                print("Devi inserire un tipo di immobile valido")
            else:
                is_valid = True

        return type_immobile.lower()

    def get_type_immobile_params(self, type_immobile: str) -> Union[int, bool]:
        print("⭐ Type Immobile", type_immobile)
        if type_immobile == "alloggio":
            return_data = self.__input_int(
                "Insersci il numero di stanze: ",
                "Devi inserire un numero valido",
                only_positive=(True, True),
            )
        elif type_immobile == "garage":
            is_valid = False
            while not is_valid:
                response = self.__input_str(
                    "Il garage è interrato? (Si, No): ", "Insersci una riposta valida"
                )

                if response.lower() == "si":
                    is_valid = True
                    return_data = True
                elif response.lower() == "no":
                    is_valid = True
                    return_data = False
                else:
                    print("❌ Devi inserire una risposta valida (Si, No)")
        print("⭐ Return data:", return_data)
        return return_data

    def __manage_menu_choiche(self):
        is_valid = False
        while not is_valid:
            choice = self.__input_int(
                "Insersci il numero della opzione da scegliere: ",
                "Insersci un numero valido",
            )

            if 1 <= choice <= 6:
                is_valid = True
            else:
                print("❌ Insersci un numero valido")

        if choice == 1:
            self.__print_immobile_by_code()
        elif choice == 2:
            self.__print_immobile_by_cost_rage()
        elif choice == 3:
            immobili = self.__agenzia.get_immobile_by_max_extension()
            self.__print_immobili(immobili)
        elif choice == 4:
            mean_tax = self.__agenzia.calculate_mean_tax()
            print(f"➗ La tassa media è pari al {mean_tax}%")
        elif choice == 5:
            self.__print_immobile_other_info()
        elif choice == 6:
            self.__exit_menu()

    def __exit_menu(self):
        self.active = False

    def __print_immobili(self, immobili: list[Immobile]) -> None:
        for immobile in immobili:
            print(immobile)

    def __print_immobile_by_code(self) -> None:
        code = self.__input_str(
            "Insersci il codice dell immobile: ", "Insersci un codice valido"
        )
        immobili = self.__agenzia.get_immobile(codice=code)
        print(f"Sono stati trovati {len(immobili)} immobili")
        self.__print_immobili(immobili)

    def __print_immobile_by_cost_rage(self) -> None:
        low_range = self.__input_float(
            "Insersci il range di costo minimo: ",
            "Insersci un costo valido",
            only_positive=(True, True),
        )
        high_range = self.__input_float(
            "Insersci il range di costo massimo: ",
            "Insersci un costo valido",
            only_positive=(True, True),
        )

        immobili = self.__agenzia.get_immobile_by_price(low_range, high_range)
        print(f"Sono stati trovati {len(immobili)} immobili")
        self.__print_immobili(immobili)

    def __print_immobile_other_info(self) -> None:
        code = self.__input_str(
            "Insersci il codice dell immobile: ",
            "Insersci un codice valido",
        )

        immobili = self.__agenzia.get_immobile(code)
        print(f"Sono stati trovati {len(immobili)} immobili")

        for immobile in immobili:
            total_cost = immobile.calcola_valore_totale()
            extension = immobile.get_estensione()
            type_name = immobile.get_type_name()
            immobile_code = immobile.get_codice()

            print(
                f"🫰 Il costo totale del {type_name} con codice {immobile_code} è pari a {total_cost} euro"
            )
            print(
                f"🏬 L'estensione dell {type_name} con codice {immobile_code} è pari a {extension} metri quadrati"
            )

    def __input_str(self, input_label: str, error_message: str) -> str:
        valid = False
        while not valid:
            try:
                data = input(f"⚪ {input_label}")
                if len(data) == 0:
                    custom_error = True
                    raise ValueError("Insersci una stringa")

                valid = True
            except ValueError as e:
                if not custom_error:
                    print("❌", error_message)
                else:
                    print(f"❌ {e}")

        return data

    def __input_int(
        self,
        input_label: str,
        error_message: str,
        only_positive=(False, False),
    ) -> int:
        valid = False
        while not valid:
            custom_error = False
            try:
                data = int(input(f"⚪ {input_label}"))
                # if only_positive and data < 0:
                #     custom_error = True
                #     raise ValueError("Devi inserire un numero maggiore o uguale a zero")

                if only_positive[0]:
                    if only_positive[1]:
                        if data <= 0:
                            custom_error = True
                            raise ValueError("Devi inserire un numero maggiore di zero")
                        valid = True
                    else:
                        if data < 0:
                            custom_error = True
                            raise ValueError(
                                "Devi inserire un numero maggiore o uguale a zero"
                            )
                        valid = True
                else:
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
        only_positive=(False, False),
    ) -> float:
        valid = False
        while not valid:
            custom_error = False
            try:
                data = float(input(f"⚪ {input_label}"))

                if only_positive[0]:
                    if only_positive[1]:
                        if data <= 0:
                            custom_error = True
                            raise ValueError("Devi inserire un numero maggiore di zero")
                        valid = True
                    else:
                        if data < 0:
                            custom_error = True
                            raise ValueError(
                                "Devi inserire un numero maggiore o uguale a zero"
                            )
                        valid = True
                else:
                    valid = True

            except ValueError as err:
                if custom_error:
                    print("❌", err)
                else:
                    print("❌", error_message)

        return data


if __name__ == "__main__":
    Menu()
