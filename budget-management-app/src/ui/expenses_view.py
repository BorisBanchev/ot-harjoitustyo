from tkinter import ttk, constants


class ExpensesView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initiliaze()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initiliaze(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame,
                          text="Here you can track your expenses!")
        label.grid(padx=10, pady=10)
