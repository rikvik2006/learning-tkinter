class Memory:
    """Memory class for storing the memory of the calculator"""

    def __init__(self):
        self.set_memory(0)

    # Restituisce l'attualve valore della memoria
    def get_memory(self) -> int:
        return self.__memory

    # Imposta il valore obligandone il tipo
    def set_memory(self, value: int) -> None:
        if isinstance(value, int):
            self.__memory = value
        else:
            raise TypeError("Memory must be an integer")

    # Aggiunge un valore dato alla memoria
    def add_to_memory(self, value: int) -> None:
        if isinstance(value, int):
            self.__memory += value
        else:
            raise TypeError("Memory must be an integer")

    # Sottrae un valore dato alla memoria
    def subtract_to_memory(self, value: int) -> None:
        if isinstance(value, int):
            self.__memory -= value
        else:
            raise TypeError("Memory must be an integer")
