from typing import Union


class Calculation:
    @staticmethod
    def calculate(expression: str) -> Union[int, float, str]:
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
