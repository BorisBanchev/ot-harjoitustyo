from tkinter import ttk, constants, StringVar
from services.expense_service import InvalidExpenseError, expense_service


class UpdateExpenseView:
    def __init__(self, root, expense, handle_update_expense, handle_back_to_expenses, handle_logout):
        self._root = root
        self._expense = expense
        self._handle_update_expense = handle_update_expense
        self._handle_back_to_expenses = handle_back_to_expenses
        self._handle_logout = handle_logout
        self._frame = None
        self._description_entry = None
        self._amount_entry = None
        self._date_combobox = None
        self._error_variable = None
        self._error_label = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.config(foreground="red")
        self._error_label.grid()

    def _show_success(self, message):
        self._error_variable.set(message)
        self._error_label.config(foreground="green")
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _update_expense_handler(self):
        description = self._description_entry.get()
        amount = self._amount_entry.get()
        date = self._date_combobox.get()

        if not description or not amount or not date:
            self._show_error("All fields are required!")
            return

        try:
            self._handle_update_expense(
                self._expense.expense_id, description, amount, date)
        except InvalidExpenseError as e:
            self._show_error(str(e))
        except Exception as e:
            self._show_error("An unexpected error occurred!")

    def _initialize_description_entry(self):
        description_label = ttk.Label(master=self._frame, text="Description")
        self._description_entry = ttk.Entry(master=self._frame)
        self._description_entry.insert(0, self._expense.description)
        description_label.grid(row=1, column=0, padx=5,
                               pady=5, sticky=constants.W)
        self._description_entry.grid(
            row=1, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize_amount_entry(self):
        amount_label = ttk.Label(master=self._frame, text="Amount")
        self._amount_entry = ttk.Entry(master=self._frame)
        self._amount_entry.insert(0, str(self._expense.amount))
        amount_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        self._amount_entry.grid(row=2, column=1, padx=5,
                                pady=5, sticky=constants.EW)


    def _initialize_date_entry(self):
        date_label = ttk.Label(master=self._frame, text="Date")
        available_dates = expense_service.get_available_dates()
        self._date_combobox = ttk.Combobox(
            master=self._frame, values=available_dates, state="readonly")
        self._date_combobox.set(self._expense.date)
        date_label.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)
        self._date_combobox.grid(
            row=3, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        greeting_label = ttk.Label(
            master=self._frame, text="Hi, update your expense!", foreground="blue")
        greeting_label.grid(row=0, column=0, columnspan=2,
                            padx=5, pady=5, sticky=constants.W)

        self._initialize_description_entry()
        self._initialize_amount_entry()
        self._initialize_date_entry()

        update_button = ttk.Button(
            master=self._frame,
            text="Update Expense",
            command=self._update_expense_handler
        )
        update_button.grid(row=4, column=0, columnspan=2,
                           padx=5, pady=5, sticky=constants.EW)

        back_button = ttk.Button(
            master=self._frame,
            text="Back to Expenses",
            command=self._handle_back_to_expenses
        )
        back_button.grid(row=5, column=0, columnspan=2,
                         padx=5, pady=5, sticky=constants.EW)

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_logout
        )
        logout_button.grid(row=6, column=0, columnspan=2,
                           padx=5, pady=5, sticky=constants.EW)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        self._error_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        self._hide_error()

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
