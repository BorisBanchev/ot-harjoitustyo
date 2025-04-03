from tkinter import ttk, constants, StringVar
from repositories.expense_repository import expense_repository
from services.user_service import user_service


class ShowExpensesView:
    def __init__(self, root, handle_add_expense):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._handle_add_expense = handle_add_expense
        self._selected_expense_id = None
        self._budget_label = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _delete_expense_handler(self):
        if self._selected_expense_id:
            expense_repository.delete_expense(self._selected_expense_id)
            self._refresh_expenses()

    def _update_expense_handler(self):
        pass

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
                text=f"Current Budget: {current_budget}€", foreground="green")

    def _refresh_expenses(self):
        for row in self._tree.get_children():
            self._tree.delete(row)

        expenses = expense_repository.get_expenses_by_user(
            user_service._user.username)
        for expense in expenses:
            self._tree.insert("", "end", values=(
                expense.id, expense.description, expense.amount, expense.date))

        self._refresh_budget()

    def _initialize_budget_field(self):
        self._budget_label = ttk.Label(
            master=self._frame, text="", foreground="green")
        self._budget_label.grid(row=0, column=0, padx=5,
                                pady=5, sticky=constants.W)

    def _initialize_expenses_table(self):
        self._tree = ttk.Treeview(
            master=self._frame,
            columns=("id", "description", "amount", "date"),
            show="headings"
        )
        self._tree.heading("id", text="ID")
        self._tree.heading("description", text="Description")
        self._tree.heading("amount", text="Amount")
        self._tree.heading("date", text="Date")
        self._tree.bind("<<TreeviewSelect>>", self._on_expense_select)
        self._tree.grid(row=1, column=0, columnspan=3,
                        padx=5, pady=5, sticky=constants.EW)

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

        self._refresh_expenses()
