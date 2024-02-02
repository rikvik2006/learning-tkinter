from distutils.core import run_setup
from pickletools import read_uint1
import re
import tkinter as Tk
from typing import Union
from tkinter import ttk
from unittest import result
from components.CalculatorButton import CalculatorButton
from utils.helpers.expression import Expression
from utils.helpers.calculation import Calculation


class ButtonsFrame(ttk.Frame):
    def __init__(self, master, layout, buttons, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(**layout)
        self.create_buttons(buttons)
        self.current_char = 0
        self.old_char = None
        self.allows_write = True
        self.write_before = False

    def create_buttons(self, buttons):
        self.widget_buttons = []

        # for row_index, row in enumerate(self.buttons):
        #     for column_index, button_text in enumerate(row):
        #         button = ttk.Button(
        #             master=self,
        #             text=button_text,
        #             style="Buttons.TButton",
        #             command=lambda text=button_text: self.master.display.add_text(text),
        #         )
        #         button.grid(row=row_index, column=column_index, sticky="nsew")

        for row_index, row in enumerate(buttons):
            for column_index, button_data in enumerate(row):
                button_text, colspan = button_data.split("|")
                rowspan = 1
                if button_text == "=":
                    colspan, rowspan = colspan.split("x")
                button = CalculatorButton(
                    master=self,
                    text=button_text,
                    style="Buttons.TButton",
                    padding="10 10 10 10",
                    # command=lambda text=button_text: self.master.components[
                    #     "display"
                    # ].add_text(text),
                )
                button.grid(
                    row=row_index,
                    column=column_index,
                    columnspan=colspan,
                    rowspan=rowspan,
                    sticky="nsew",
                )
                self.widget_buttons.append(button)

                # Aggiungo al bottone l'evento di click con il tasto sinitro del mouse
                button.bind("<Button-1>", lambda event: self.on_click(event=event))

    # Metodo di callback per l'evento di click con il tasto sinitro del mouse di un bottone
    def on_click(self, event: Tk.Event):
        # In base al testo del bottone eseguiamo l'azione corrispondente
        display = self.master.components["display"]
        info_display = self.master.components["info_display"]
        if event.widget["text"] == "C":
            self.__set_to_normal_state(current_char=0, old_char=None)
            self.write_before = False
            display.clear()
        elif event.widget["text"] == "=":
            self.__on_click_equal()
        elif event.widget["text"] == "BC":
            self.__set_to_normal_state(current_char=self.old_char, old_char=None)
            if not self.write_before:
                display.backspace()
            else:
                print("Write backward")
                display.backspace_reverse()
        elif event.widget["text"] == "MEM":
            self.__display_memory()
        elif event.widget["text"] == "STO":
            self.__store_to_memory()
        elif event.widget["text"] == "M+":
            self.__add_to_memory()

        elif event.widget["text"] == "sin":
            # self.__calculate_sine()
            self.__display_result(calculation=Calculation.sine, ndigits=4)
        elif event.widget["text"] == "cos":
            # self.__calculate_cosine()
            self.__display_result(calculation=Calculation.cosine, ndigits=4)
        elif event.widget["text"] == "tan":
            # self.__calculate_tangent()
            self.__display_result(calculation=Calculation.tangent, ndigits=4)
        elif event.widget["text"] == "!":
            # self.__calculate_factorial()
            self.__display_result(calculation=Calculation.factorial, ndigits=0)
        elif event.widget["text"] == "x²":
            self.__display_result(calculation=Calculation.square_power, ndigits=4)
        elif event.widget["text"] == "xⁿ":
            self.__calculate_n_power()
        elif event.widget["text"] == "√":
            self.__display_result(calculation=Calculation.square_root, ndigits=4)
        elif event.widget["text"] == "ⁿ√":
            self.__calculate_n_root()
        elif event.widget["text"] == "1/x":
            # self.__calculate_mutual()
            self.__display_result(calculation=Calculation.mutual, ndigits=6)
        else:
            if not self.allows_write:
                return

            button_text = event.widget["text"]
            self.old_char = self.current_char
            self.current_char = button_text
            if not self.write_before:
                display.add_text(event.widget["text"])
            else:
                display.add_backwards_text(event.widget["text"])
            if Expression.is_symbol(self.current_char) and Expression.is_symbol(
                self.old_char
            ):
                self.allows_write = False
                info_display.set_err("Errore di sintassi")

    # Mostra il contenuto della memoria sul display
    def __display_memory(self):
        memory_number = self.master.memory.get_memory()
        display = self.master.components["display"]

        # Se il display è vuoto quindi contiene 0 il contenuto della memoria sotituisce lo 0.
        # Se l'ultimo carattere del display è un operatore il contenuto della memoria viene aggiunto al display.
        # Altrimenti se nel display è presente un numero oppure un numero incompleto, il contenuto della memoria viene sotiutito al contenuto attuale
        if display.get_text() == "0":
            display.set_text(str(memory_number))
        elif Expression.is_operator(display.get_text()[-1]):
            if memory_number < 0:
                display.add_text("(" + str(memory_number) + ")")
            else:
                display.add_text(str(memory_number))
        else:
            display.set_text(str(memory_number))

        self.__set_to_normal_state(
            current_char=memory_number, old_char=self.current_char
        )
        print("📝 Memory number", memory_number)

    # Salva il numero attuale nel display nella memoria (se è presente una espressione viene salvato solo l'ultimo numero)
    def __store_to_memory(self):
        display = self.master.components["display"]
        memory = self.master.memory
        display_current_text = display.get_text()
        numbers = Expression.get_expressions_numbers(display_current_text)
        print("☕", numbers)
        memory.set_memory(numbers[-1])
        print("🔗 Saved value", memory.get_memory())

    # Esegue una somma algebrica con il numero contenuto in memoria e quello mostrato nel display
    # (se è presente una espressione viene sommato solo l'ultimo numero con il contenuto della memoria)
    def __add_to_memory(self):
        display = self.master.components["display"]
        memory = self.master.memory
        display_current_text = display.get_text()
        numbers = Expression.get_expressions_numbers(display_current_text)
        print("☕", numbers)
        memory.add_to_memory(numbers[-1])
        print("🔗 Saved value", memory.get_memory())

    def __on_click_equal(self):
        display = self.master.components["display"]
        info_display = self.master.components["info_display"]
        display_current_text = display.get_text()
        result = self.__calculate_result(display_current_text)

        if isinstance(result, (int, float)):
            result = round(result, 4)
            display.set_text(str(result))
        elif isinstance(result, str):
            info_display.set_err(result)

    def __calculate_result(self, expression: str) -> Union[int, float, str]:
        if not ("^" in expression) and not ("√" in expression):
            result = Calculation.calculate(expression)
            print("➕", result)
            print("🫶", type(result))

            if isinstance(result, (int, float)):
                if isinstance(result, float):
                    result = Expression.remove_blank_floatingpoints(result)
                self.__set_to_normal_state(current_char=result, old_char=None)
            elif isinstance(result, str):
                self.__set_to_normal_state(current_char=0, old_char=None)
        elif "^" in expression and not ("√" in expression):
            base, exponent = expression.split("^")
            exponent = Calculation.calculate(exponent)
            if isinstance(exponent, str):
                self.__set_to_normal_state(current_char=0, old_char=None)
                return exponent
            elif isinstance(exponent, (int, float)):
                base = base.replace("(", "").replace(")", "")
                base = Expression.convert_string_numbers_to_numbers([base])[0]
                result = Calculation.power_of_n(base, exponent)

                if isinstance(result, (int, float)):
                    if isinstance(result, float):
                        result = Expression.remove_blank_floatingpoints(result)
                    self.__set_to_normal_state(current_char=result, old_char=None)
                elif isinstance(result, (str, complex)):
                    self.__set_to_normal_state(current_char=0, old_char=None)
                    if isinstance(result, complex):
                        result = "Impossibile fuori dominio"
        elif "√" in expression and not ("^" in expression):
            self.write_before = False
            root_exponent, root_number = expression.split("√")
            root_exponent = Calculation.calculate(root_exponent)
            if isinstance(root_exponent, str):
                self.__set_to_normal_state(current_char=0, old_char=None)
                return root_exponent
            elif isinstance(root_exponent, (int, float)):
                root_number = root_number.replace("(", "").replace(")", "")
                root_number = Expression.convert_string_numbers_to_numbers(
                    [root_number]
                )[0]
                result = Calculation.n_square_root(root_number, root_exponent)

                if isinstance(result, (int, float)):
                    if isinstance(result, float):
                        result = Expression.remove_blank_floatingpoints(result)
                    self.__set_to_normal_state(current_char=result, old_char=None)
                elif isinstance(result, str):
                    self.__set_to_normal_state(current_char=0, old_char=None)
        else:
            result = "Errore di sintassi"
        return result

    # def __calculate_result_n_root(self, expression: str) -> Union[int, float, str]:
    #     if not ("√" in expression):
    #         result = Calculation.calculate(expression)

    # Serve per modificare l'ho stato della calcolatrice modificando gli utilmi due caratteri inseriti, questo serve per gestire gli errori
    def __set_to_normal_state(self, current_char, old_char):
        info_display = self.master.components["info_display"]
        self.current_char = current_char
        self.old_char = old_char
        self.allows_write = True
        info_display.clear_err()

    def __display_result(self, calculation, ndigits=0):
        display = self.master.components["display"]
        info_display = self.master.components["info_display"]
        display_current_text = display.get_text()
        result = self.__calculate_result(display_current_text)

        if isinstance(result, (int, float)):
            result = calculation(result)
            if isinstance(result, (int, float)):
                if ndigits > 0:
                    result = round(result, ndigits)
                if isinstance(result, float):
                    result = Expression.remove_blank_floatingpoints(result)
                display.set_text(str(result))
            elif isinstance(result, str):
                info_display.set_err(result)
        elif isinstance(result, str):
            info_display.set_err(result)

    def __calculate_n_power(self):
        display = self.master.components["display"]
        info_display = self.master.components["info_display"]
        display_current_text = display.get_text()
        result = self.__calculate_result(display_current_text)

        if isinstance(result, (int, float)):
            display.set_text(f"({result})^")
        elif isinstance(result, str):
            info_display.set_err(result)

    def __calculate_n_root(self):
        display = self.master.components["display"]
        info_display = self.master.components["info_display"]
        display_current_text: str = display.get_text()
        result = self.__calculate_result(display_current_text)

        print("🔗", self.write_before)
        self.write_before = True
        if isinstance(result, (int, float)):
            display.set_text(f"√({result})")
        elif isinstance(result, str):
            info_display.set_err(result)
            self.write_before = False
            print("🔗", self.write_before)
