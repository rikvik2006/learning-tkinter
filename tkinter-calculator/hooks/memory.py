class Memory:
    """Memory class for storing the memory of the calculator"""

    def __init__(self, master):
        self.master = master
        self.set_memory(0)

    # Restituisce l'attualve valore della memoria
    def get_memory(self) -> int:
        return self.__memory

    # Imposta il valore obligandone il tipo
    def set_memory(self, value: int) -> None:
        if isinstance(value, int) or isinstance(value, float):
            self.__memory = value

            if value != 0:
                self.master.components["info_display"].set_memory_indicator(True)
            else:
                self.master.components["info_display"].set_memory_indicator(False)
        else:
            raise TypeError("Memory must be an integer or a float")

    # Aggiunge un valore dato alla memoria
    def add_to_memory(self, value: int) -> None:
        if isinstance(value, int) or isinstance(value, float):
            self.__memory += value
        else:
            raise TypeError("Memory must be an integer or a float")

    # Sottrae un valore dato alla memoria
    def subtract_to_memory(self, value: int) -> None:
        if isinstance(value, int) or isinstance(value, float):
            self.__memory -= value
        else:
            raise TypeError("Memory must be an integer or a float")
