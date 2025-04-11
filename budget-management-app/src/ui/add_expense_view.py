from tkinter import ttk, constants, StringVar
from datetime import datetime, timedelta
from services.user_service import user_service
from repositories.expense_repository import expense_repository
from entities.expense import Expense
from services.expense_service import InvalidExpenseError


class AddExpenseView:
    def __init__(self, root, handle_expense_adding, handle_show_expenses, handle_logout):
        self._root = root
        self._frame = None
        self._handle_expense_adding = handle_expense_adding
        self._handle_show_expenses = handle_show_expenses
        self._handle_logout = handle_logout
        self._expense_description_entry = None
        self._expense_amount_entry = None
        self._expense_date_combobox = None
        self._error_variable = None
        self._error_label = None
        self._message_label = None
        self._initialiaze()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _set_budget_handler(self):
        budget = self._budget_entry.get()

        if not budget:
            self._show_error("Budget is required!")
            return
        try:
            user_service.set_budget(user_service._user.username, budget)
            self._show_success("Budget set successfully!")
            self._refresh_message()
        except Exception as e:
            self._show_error(str(e))

    def _add_expense_handler(self):
        description = self._expense_description_entry.get()
        amount = self._expense_amount_entry.get()
        date = self._expense_date_combobox.get()

        if not description or not amount or not date:
            self._show_error(
                "An expense must have description, amount and date!")
            return

        try:
            self._handle_expense_adding(description, amount, date)
            self._show_success("Expense added successfully!")
            self._clear_form()
        except InvalidExpenseError as e:
            self._show_error(str(e))
        except Exception as e:
            self._show_error("An unexpected error occured!")

    def _refresh_message(self):
        if user_service._user.monthly_budget is None:
            self._message_label.config(
                text=f"Hey {user_service._user.username}, set a budget!")
        else:
            self._message_label.config(
                text=f"Hey {user_service._user.username}, add an expense!")

    def _clear_form(self):
        self._expense_description_entry.delete(0, constants.END)
        self._expense_amount_entry.delete(0, constants.END)
        self._expense_date_combobox.set("")

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

    def _get_available_dates(self):
        # Generate a list of dates from current day to the end of the month
        today = datetime.now()
        last_day_of_month = (today.replace(
            day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
        return [(today + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((last_day_of_month - today).days + 1)]

    def _initialiaze_description(self):
        description_label = ttk.Label(
            master=self._frame, text="Expense Description")
        self._expense_description_entry = ttk.Entry(master=self._frame)
        description_label.grid(row=3, column=0, padx=5,
                               pady=5, sticky=constants.W)
        self._expense_description_entry.grid(
            row=3, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialiaze_amount(self):
        amount_label = ttk.Label(master=self._frame, text="Amount")
        self._expense_amount_entry = ttk.Entry(master=self._frame)
        amount_label.grid(row=4, column=0, padx=5, pady=5, sticky=constants.W)
        self._expense_amount_entry.grid(
            row=4, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialiaze_date(self):
        date_label = ttk.Label(master=self._frame, text="Date")
        date_label.grid(row=5, column=0, padx=5, pady=5, sticky=constants.W)

        available_dates = self._get_available_dates()
        self._expense_date_combobox = ttk.Combobox(
            master=self._frame, values=available_dates, state="readonly")
        self._expense_date_combobox.grid(
            row=5, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize_budget(self):
        budget_label = ttk.Label(master=self._frame, text="Set Monthly Budget")
        self._budget_entry = ttk.Entry(master=self._frame)
        budget_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        self._budget_entry.grid(row=1, column=1, padx=5,
                                pady=5, sticky=constants.EW)

        set_budget_button = ttk.Button(
            master=self._frame,
            text="Set Budget",
            command=self._set_budget_handler
        )
        set_budget_button.grid(row=2, column=0, columnspan=2,
                               padx=5, pady=5, sticky=constants.EW)

    def _initialiaze_form(self):
        self._initialiaze_description()
        self._initialiaze_amount()
        self._initialiaze_date()

        add_button = ttk.Button(
            master=self._frame,
            text="Add Expense",
            command=self._add_expense_handler
        )
        add_button.grid(row=6, column=0, padx=5, pady=5, sticky=constants.EW)

    def _initialiaze(self):
        self._frame = ttk.Frame(master=self._root)

        self._message_label = ttk.Label(
            master=self._frame, text="", foreground="blue")
        self._message_label.grid(
            row=0, column=0, columnspan=2,  padx=5, pady=5, sticky=constants.W)
        self._refresh_message()

        self._initialize_budget()

        self._initialiaze_form()

        show_expenses_button = ttk.Button(
            master=self._frame,
            text="Show Expenses",
            command=self._handle_show_expenses
        )
        show_expenses_button.grid(
            row=7, column=0, padx=5, pady=5, sticky=constants.EW)

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_logout
        )
        logout_button.grid(row=8, column=0, padx=5,
                           pady=5, sticky=constants.EW)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        self._error_label.grid(row=9, column=0, padx=5, pady=5)
        self._hide_error()

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
