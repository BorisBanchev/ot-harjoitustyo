from tkinter import ttk, constants
from services.expense_service import expense_service
from services.user_service import user_service


class ShowExpensesView:
    '''Kulujen näyttämisestä vastaava näkymä'''

    def __init__(self, root, handle_add_expense, handle_logout, handle_update_expense):
        ''' Luokan konstruktori, joka luo uuden kulujen näyttämisnäkymän
        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan
            handle_add_expense:
                Kutsuttava-funktio, jota kutsutaan kun käyttäjä painaa add expense-nappia ja 
                hänet ohjataa kulun lisäys näkymään
            handle_logout:
                Kutsuttava-funktio, jota kutsutaan kun käyttäjä kirjautuu ulos ja hänet ohjataa login-näkymään
            handle_update_expense:
                Kutsuttava-funktio, jota kutsutaan kun käyttäjä valitsee muokkaa kulua, ja hänet ohjataa kulun muokkaus
                näkymään

        '''
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._handle_add_expense = handle_add_expense
        self._handle_logout = handle_logout
        self._handle_update_expense = handle_update_expense
        self._selected_expense_id = None
        self._budget_label = None
        self._initialize()

    def pack(self):
        '''Näyttää näkymän'''
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        '''Tuhoaa näkymän'''
        self._frame.destroy()

    def _delete_expense_handler(self):
        if self._selected_expense_id:
            expense_service.delete_expense(self._selected_expense_id)
            self._refresh_expenses()

    def _update_expense_handler(self):
        if not self._selected_expense_id:
            return

        expenses = expense_service.get_expenses_by_user(
            user_service._user.username)
        selected_expense = next(
            (expense for expense in expenses if expense.expense_id ==
             int(self._selected_expense_id)),
            None
        )
        if selected_expense:
            self._handle_update_expense(selected_expense)

    def _on_expense_select(self, event):
        selected_expense = self._tree.selection()
        if selected_expense:
            self._selected_expense_id = self._tree.item(
                selected_expense, "values")[0]

    def _refresh_budget(self):
        if user_service._user.monthly_budget is None:
            self._budget_label.config(text="Budget not set!", foreground="red")

        else:
            current_budget = user_service.get_current_budget()
            self._budget_label.config(
                text=f"Current Budget: {current_budget:.2f}€", foreground="green")

    def _refresh_expenses(self):
        for row in self._tree.get_children():
            self._tree.delete(row)

        expenses = expense_service.get_expenses_by_user(
            user_service._user.username)
        sorted_expenses = sorted(
            expenses, key=lambda expense: expense.amount, reverse=True)
        for expense in sorted_expenses:
            self._tree.insert("", "end", values=(
                expense.expense_id, expense.description, expense.amount, expense.date))

        self._refresh_budget()

    def _initialize_budget_field(self):
        self._budget_label = ttk.Label(
            master=self._frame, text="", foreground="green")
        self._budget_label.grid(row=0, column=0, padx=5,
                                pady=5, sticky=constants.W)

    def _initialize_expenses_table(self):
        table_frame = ttk.Frame(master=self._frame)
        table_frame.grid(row=1, column=0, columnspan=3,
                         padx=5, pady=5, sticky=constants.EW)

        self._tree = ttk.Treeview(
            master=table_frame,
            columns=("id", "description", "amount", "date"),
            show="headings",
            selectmode="browse"
        )
        self._tree.heading("id", text="ID")
        self._tree.heading("description", text="Description")
        self._tree.heading("amount", text="Amount")
        self._tree.heading("date", text="Date")
        self._tree.bind("<<TreeviewSelect>>", self._on_expense_select)

        scrollbar = ttk.Scrollbar(
            master=table_frame,
            orient="vertical",
            command=self._tree.yview
        )
        self._tree.configure(yscrollcommand=scrollbar.set)

        self._tree.grid(row=0, column=0, sticky=constants.NSEW)
        scrollbar.grid(row=0, column=1, sticky=constants.NS)

        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_rowconfigure(0, weight=1)

    def _initialize(self):
        self._initialize_budget_field()
        self._initialize_expenses_table()

        delete_button = ttk.Button(
            master=self._frame,
            text="Delete Expense",
            command=self._delete_expense_handler
        )
        delete_button.grid(row=2, column=0, padx=5,
                           pady=5, sticky=constants.EW)

        add_expense_button = ttk.Button(
            master=self._frame,
            text="Add Expense",
            command=self._handle_add_expense
        )
        add_expense_button.grid(row=2, column=2, padx=5,
                                pady=5, sticky=constants.EW)

        update_button = ttk.Button(
            master=self._frame,
            text="Update Expense",
            command=self._update_expense_handler
        )
        update_button.grid(row=2, column=1, padx=5,
                           pady=5, sticky=constants.EW)

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_logout
        )
        logout_button.grid(row=3, column=0, padx=5,
                           pady=5, sticky=constants.EW)

        self._refresh_expenses()

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
