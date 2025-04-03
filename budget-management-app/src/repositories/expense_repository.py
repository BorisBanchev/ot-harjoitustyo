from entities.expense import Expense
from db.database_connection import get_database_connection


class ExpenseRepository:
    def __init__(self, db):
        self._db = db

    def create_expense(self, expense: Expense, username: str):
        cursor = self._db.cursor()
        cursor.execute('''
            INSERT INTO expenses (description, amount, date, username)
            VALUES (?, ?, ?, ?)
        ''', (expense.description, expense.amount, expense.date, username))
        self._db.commit()

    def get_expenses_by_user(self, username: str):
        cursor = self._db.cursor()
        cursor.execute('''
            SELECT * FROM expenses WHERE username = ?
        ''', (username, ))
        rows = cursor.fetchall()
        return [Expense(row["description"], row["amount"], row["date"], row["id"]) for row in rows]

    def delete_expense(self, expense_id: int):
        cursor = self._db.cursor()
        cursor.execute('''
            DELETE FROM expenses WHERE id = ?
        ''', (expense_id, ))
        self._db.commit()


expense_repository = ExpenseRepository(get_database_connection())
