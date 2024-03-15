import customtkinter as ctk
from typing import Union, Literal
from PIL import Image
from pathlib import Path


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

    # type: Literal["autovettura", "autocarro", "motovettura"]
    def __init__(self, model: str, price: float, nameplate: str, brand: str, number_seats: int, base: float, other: Union[int, float, None]) -> None:
        self.__type = type
        self.__model = model
        self.__price = price
        self.__nameplate = nameplate
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

        # if type == "autovettura":
        #     img_path = Path.joinpath(Path.cwd(), "img", "tabler-icon-car.png")
        # elif type == "autocarro":
        #     img_path = Path.joinpath(Path.cwd(), "img", "tabler-icon-tir.png")
        # elif type == "motovettura":
        #     img_path = Path.joinpath(Path.cwd(), "img", "tabler-icon-motorbike.png")
        
        img_path = Path.joinpath(Path.cwd(), "img", "tabler-icon-car.png")

        self.__product_image = ctk.CTkImage(light_image=Image.open(img_path))
        
        # if not isinstance(img_path, str):
        #     raise ValueError("insersci un type corretto")
        
        return [
            {
                "value": self.__product_image,
                "padx": (40, 0)
            },
            {
                "value": self.__model,
                "padx": (100, 0),         
            },
            {
                "value": self.__price,
                "padx": (200, 0),         
            },
            {
                "value": self.__nameplate,
                "padx": (100, 0),         
            },
            {
                "value": self.__brand,
                "padx": (200, 0),         
            },
            {
                "value": self.__number_seats,
                "padx": (100, 0),         
            },
            {
                "value": self.__base,
                "padx": (100, 0),         
            },
            {
                "value": self.__other,
                "padx": (100, 15),         
            },
        ]
    