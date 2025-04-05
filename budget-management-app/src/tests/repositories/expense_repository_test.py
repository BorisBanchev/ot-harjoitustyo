import unittest
from entities.user import User
from entities.expense import Expense
from repositories.user_repository import user_repository
from repositories.expense_repository import expense_repository


class TestExpenseRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()
        expense_repository.delete_all_expenses()
        self.user_paavo = User("paavo", "1234")
        self.expense = Expense("car", 2000, "2025-04-08", 2)

    def test_create_expense(self):
        user_repository.create_user(self.user_paavo)
        user_by_name = user_repository.get_user_by_name("paavo")
        username = user_by_name.username

        expenses_by_user = expense_repository.get_expenses_by_user(username)
        self.assertEqual(len(expenses_by_user), 0)

        expense_repository.create_expense(self.expense, username)

        expenses_by_user_after = expense_repository.get_expenses_by_user(
            username)
        self.assertEqual(len(expenses_by_user_after), 1)

    def test_delete_expense(self):
        user_repository.create_user(self.user_paavo)
        user_by_name = user_repository.get_user_by_name("paavo")
        username = user_by_name.username
        expense_repository.create_expense(self.expense, username)

        expenses_by_user = expense_repository.get_expenses_by_user(username)
        self.assertEqual(len(expenses_by_user), 1)

        expense_repository.delete_expense(expenses_by_user[0].id)
        expenses_by_user_after = expense_repository.get_expenses_by_user(
            username)
        self.assertEqual(len(expenses_by_user_after), 0)
