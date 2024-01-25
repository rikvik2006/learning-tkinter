class LayoutPositionGrid:
    def __init__(self, row=0, column=0, sticky="nsew"):
        self.row = row
        self.column = column
        self.sticky = sticky

    def __call__(self) -> dict:
        return {
            "row": self.row,
            "column": self.column,
            "sticky": self.sticky,
        }
