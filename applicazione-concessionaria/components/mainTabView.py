import customtkinter as ctk


class MainTabView(ctk.CTkTabview):
    """Rappresent the main tab view"""

    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

    def __add_tabs(self):
        self.add("")
