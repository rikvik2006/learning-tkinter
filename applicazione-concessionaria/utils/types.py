from typing import Union

class LayoutPositionGrid:
    def __init__(self, row=0, column=0, sticky="nsew"):
        self.row = row
        self.column = column
        self.sticky = sticky

    def __call__(self) -> dict:
        return dict({
            "row": self.row,
            "column": self.column,
            "sticky": self.sticky,
        })
    
class RowTableData():
    """Type for table data in client tab"""

    def __init__(self, model: str, price: float, nameplate: str, brand: str, number_seats: int, base: float, other: Union[int, float, None]) -> None:
        self.__model = model
        self.__price = price
        self.__nameplate = nameplate,
        self.__brand = brand
        self.__number_seats = number_seats
        self.__base = base,
        self.__other = other

    def __call__(self) -> list:
        # return {
        #     "model": self.__model,
        #     "price": self.__price,
        #     "nameplate": self.__nameplate,
        #     "brand": self.__brand,
        #     "number_seats": self.__number_seats,
        #     "base": self.__base,
        #     "other": self.__other
        # }

        return [
            {
                "value": self.__model,
                "padx": (20, 0),         
            },
            {
                "value": self.__price,
                "padx": (20, 0),         
            },
            {
                "value": self.__nameplate,
                "padx": (20, 0),         
            },
            {
                "value": self.__brand,
                "padx": (20, 0),         
            },
            {
                "value": self.__number_seats,
                "padx": (20, 0),         
            },
            {
                "value": self.__base,
                "padx": (20, 0),         
            },
            {
                "value": self.__other,
                "padx": (20, 0),         
            },
        ]
    