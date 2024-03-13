import customtkinter as ctk


class TabViewFrame(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(column=0, row=0, padx=20, pady=20)
        self.__add_view()
        self.configure(
            fg_color="#282830",
            segmented_button_fg_color="#3A3A3A",
            segmented_button_unselected_color="#33333A",
            segmented_button_selected_color="#33333A",
        )

    def __add_view(self):
        self.add("Cliente")
        self.add("Operatore")
        self.set("Cliente")

    def __load_tab_cliente(self):
        master_view = self.tab("Cliente")
