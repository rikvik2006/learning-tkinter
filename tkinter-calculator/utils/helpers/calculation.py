from typing import Union


class Calculation:
    @staticmethod
    def calculate(expression: str) -> Union[int, float, str]:
        try:
            result = eval(expression)
            return_value = result
        except ZeroDivisionError as err:
            print("❌", err)
            return_value = "Zero Division Error"
        except Exception as err:
            print("❌", err.__doc__)
            return_value = err.__doc__

        return return_value
