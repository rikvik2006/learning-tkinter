from typing import Any
import customtkinter as ctk
from components.tabViewFrame import TabViewFrame

class LoadComponents():
    """Load components in a  specifyed Frame"""

    def loads(self, master: Any):
        TabViewFrame(master=master)