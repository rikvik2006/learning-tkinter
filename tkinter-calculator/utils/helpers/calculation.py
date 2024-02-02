import math
from typing import Union


class Calculation:
    """Class that contains the methods to calculate the expression."""

    # Questo metodo staico viene utilizzato solo per calcolare le espressioni con i classici operatori
    @staticmethod
    def calculate(expression: str) -> Union[int, float, str]:
        """Calculate the expression passed as argument with eval() function."""

        try:
            result = eval(expression)
            return_value = result
        except ZeroDivisionError as err:
            print("❌", err)
            return_value = "Divisione per 0"
        except Exception as err:
            print("❌", err.__doc__)
            # return_value = err.__doc__
            return_value = "Errore di sintassi"

        return return_value

    # Calcola la radice quadrata di un numero nei numeri reali
    @staticmethod
    def square_root(number: Union[int, float]) -> Union[int, float, str]:
        """Calculate the square root of a real number."""

        try:
            result = math.sqrt(number)
        except ValueError as err:
            print("❌", err)
            result = "Impossibile fuori dominio"
        except Exception as err:
            print("❌", err.__doc__)
            result = "Errore di sintassi"

        return result

    def n_square_root(
        number: Union[int, float], n: Union[int, float]
    ) -> Union[int, float, str]:
        try:
            result = number ** (1 / n)
            if isinstance(result, complex):
                result = "Impossibile fuori dominio"
        except ValueError as err:
            print("❌", err)
            result = "Impossibile fuori dominio"
        except Exception as err:
            print("❌", err.__doc__)
            result = "Errore di sintassi"

        return result

    # Calcola la la potenza quadrata di un numero
    @staticmethod
    def square_power(number: Union[int, float]) -> Union[int, float, str]:
        """Calculate the square power of a number."""

        try:
            result = number**2
        except Exception as err:
            print("❌", err.__doc__)
            result = "Errore di sintassi"

        return result

    # Calcola la potenza di un numero con un esponente personalizzato
    @staticmethod
    def power_of_n(
        number: Union[int, float], power: Union[int, float, str]
    ) -> Union[int, float]:
        """Calculate the power of a number, with a custom exponent."""

        try:
            result = number**power
        except Exception as err:
            print("❌", err.__doc__)
            result = "Errore di sintassi"

        return result

    # Calcola il fattoriale di un numero (intero positivo)
    def factorial(number: int) -> Union[int, float, str]:
        try:
            if isinstance(number, int):
                if number >= 0:
                    result = math.factorial(number)
                else:
                    result = "Impossibile fuori dominio"
            else:
                result = "Non definito per numeri decimali"
        except Exception as err:
            result = "Errore di sintassi"

        return result

    # Calcola il reciproco di un numero
    def mutual(number: Union[int, float]) -> Union[int, float, str]:
        try:
            if number == 0:
                result = "Impossibile fuori dominio"
            else:
                result = 1 / number
        except Exception as err:
            result = "Errore di sintassi"

        return result

    # Funzioni gognometriche
    # Calcola il seno di un numero
    @staticmethod
    def sine(number: Union[int, float]) -> Union[int, float, str]:
        try:
            radiant = math.radians(number)
            result = math.sin(radiant)
        except Exception as err:
            result = "Errore di sintassi"

        return result

    # Calcola il coseno di un numero
    @staticmethod
    def cosine(number: Union[int, float]) -> Union[int, float, str]:
        try:
            radiant = math.radians(number)
            result = math.cos(radiant)
        except Exception as err:
            result = "Errore di sintassi"

        return result

    # Calcola la tangente di un numero
    # TODO: Gestione il domino
    @staticmethod
    def tangent(number: Union[int, float]) -> Union[int, float, str]:
        try:
            if (number % 90 == 0) or (number % 180 == 0):
                result = "Impossbile fuori dominio"
            else:
                radiant = math.radians(number)
                result = math.tan(radiant)
        except Exception as err:
            result = "Errore di sintassi"

        return result
