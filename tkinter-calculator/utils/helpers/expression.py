import re
from typing import Union


class Expression:
    """Helper class for expression handling"""

    @staticmethod
    def is_operator(char: str):
        """Checks if a character is an operator"""
        return char in ["+", "-", "*", "/"]

    @staticmethod
    def is_digit(char: str):
        """Checks if a character is a digit"""
        return char in [str(i) for i in range(10)]

    @staticmethod
    def is_dot(char: str):
        """Checks if a character is a dot"""
        return char == "."

    @staticmethod
    def has_dot(number: str):
        """Checks if a number has a dot"""
        return "." in number

    @staticmethod
    def is_parenthesis(char: str):
        """Checks if a character is a parenthesis"""
        return char in ["(", ")"]

    def is_symbol(char: str):
        """Checks if a character is a symbol"""
        return char in ["+", "-", "*", "/", "(", ")", "."]

    @staticmethod
    def is_valid(char: str):
        """Checks if a character is valid"""
        return (
            Expression.is_operator(char)
            or Expression.is_digit(char)
            or Expression.is_dot(char)
            or Expression.is_parenthesis(char)
        )

    @staticmethod
    def is_empty(expression: str):
        """Checks if an expression is empty"""
        return expression == ""

    @staticmethod
    def is_valid_expression(expression: str):
        """Checks if an expression is valid"""
        if Expression.is_empty(expression):
            return False

        if not Expression.is_valid(expression[0]):
            return False

        if not Expression.is_valid(expression[-1]):
            return False

        for i in range(len(expression) - 1):
            if not Expression.is_valid(expression[i]) and not Expression.is_valid(
                expression[i + 1]
            ):
                return False

        return True

    # Converte una lista di numeri stringhe in numeri, se sono interi li converte in interi, se sono float li converte in float
    @staticmethod
    def convert_string_numbers_to_numbers(
        numbers: list[str],
    ) -> list[Union[int, float]]:
        """Converts a list of string numbers to numbers"""
        converted_numbers = []
        for number in numbers:
            if Expression.has_dot(number):
                converted_numbers.append(float(number))
            else:
                converted_numbers.append(int(number))
        return converted_numbers

    # Rimuove il punto decimale da un numero se è un intero es: 1.0 -> 1
    def remove_blank_floatingpoints(number: float) -> Union[int, float]:
        """Removes the floating point from a number if it is an integer"""
        if number.is_integer():
            return int(number)
        return number

    @staticmethod
    def get_expressions_numbers(expression: str) -> list[Union[int, float]]:
        """Returns a list of numbers from an expression, removing operators"""
        # Regex che trova tutti i numeri all'interno di una stringa (es. "1+2" -> ["1", "+2"]), compresi i numeri negativi (es. "-1+2" -> ["-1", "+2"])
        # Matenere il segno è utile perché altrimenti non potremmo sapere se il numero è negativo o positivo
        # Prova la regex su https://regexr.com/7r9bs
        regex = r"[+-]?\b\d+(?:\.\d+)?\b"
        numbers = re.findall(regex, expression, flags=re.MULTILINE)
        # Utilizzo il metodo statico della classe helper per convertire i numeri da stringhe a numeri, ma se sono degli interi li converto in interi mentre se sono dei float li converto in float
        return Expression.convert_string_numbers_to_numbers(numbers)
