from entities.expense import Expense
from repositories.expense_repository import expense_repository


class InvalidExpenseError(Exception):
    pass


class ExpenseService:
    def __init__(self, expense_repository):
        self._expense_repository = expense_repository

    def add_expense(self, description, amount, date, username):
        if not description or not amount or not date:
            raise InvalidExpenseError("All fields are required!")

        try:
            amount = float(amount)
            if amount <= 0:
                raise InvalidExpenseError("Amount must be greater than zero!")
        except ValueError:
            raise InvalidExpenseError("Amount must be a valid number!")

        expense = Expense(description=description, amount=amount, date=date)
        self._expense_repository.create_expense(expense, username)

    def update_expense(self, expense_id, description, amount, date):
        if not description or not amount or not date:
            raise InvalidExpenseError("All fields are required!")

        try:
            amount = float(amount)
            if amount <= 0:
                raise InvalidExpenseError("Amount must be greater than zero!")
        except ValueError:
            raise InvalidExpenseError("Amount must be a valid number!")

        expense_repository.update_expense(
            expense_id, description, amount, date)


expense_service = ExpenseService(expense_repository)
