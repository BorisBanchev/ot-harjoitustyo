import unittest
from entities.user import User
from entities.expense import Expense
from repositories.user_repository import user_repository
from repositories.expense_repository import expense_repository
from services.expense_service import expense_service
from services.user_service import user_service
from services.expense_service import InvalidExpenseError


class TestExpenseService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()
        expense_repository.delete_all_expenses()
        user_service.logout()
        self.valid_user = User("Paavo", "1234")
        self.invalid_user = User("Moi", "123")
        self.expense = Expense("car", 2000, "2025-04-08")

    def test_add_expense_with_valid_data_works(self):
        user_service.create_user(
            self.valid_user.username, self.valid_user.password, self.valid_user.password)
        user = user_service.login(
            self.valid_user.username, self.valid_user.password)
        user_service.set_budget(user.username, 3000)

        expense_service.add_expense(
            self.expense.description, self.expense.amount, self.expense.date, self.valid_user.username)

        expenses = expense_repository.get_expenses_by_user(
            self.valid_user.username)
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0].description, "car")

    def test_add_expense_fails_with_missing_fields(self):
        user_service.create_user(
            self.valid_user.username, self.valid_user.password, self.valid_user.password)
        user = user_service.login(
            self.valid_user.username, self.valid_user.password)

        with self.assertRaises(InvalidExpenseError) as context:
            expense_service.add_expense(
                "", self.expense.amount, self.expense.date, self.valid_user.username)
        self.assertEqual(str(context.exception), "All fields are required!")

        with self.assertRaises(InvalidExpenseError) as context:
            expense_service.add_expense(
                self.expense.description, "", self.expense.date, self.valid_user.username)
        self.assertEqual(str(context.exception), "All fields are required!")

        with self.assertRaises(InvalidExpenseError) as context:
            expense_service.add_expense(
                self.expense.description, self.expense.amount, "", self.valid_user.username)
        self.assertEqual(str(context.exception), "All fields are required!")

    def test_add_expense_fails_with_non_positive_amount(self):
        user_service.create_user(
            self.valid_user.username, self.valid_user.password, self.valid_user.password)
        user_service.login(
            self.valid_user.username, self.valid_user.password)

        with self.assertRaises(InvalidExpenseError) as context:
            expense_service.add_expense(
                self.expense.description, 0, self.expense.date, self.valid_user.username)
        self.assertEqual(str(context.exception),
                         "Amount must be greater than zero!")

        with self.assertRaises(InvalidExpenseError) as context:
            expense_service.add_expense(
                self.expense.description, -100, self.expense.date, self.valid_user.username)
        self.assertEqual(str(context.exception),
                         "Amount must be greater than zero!")

    def test_add_expense_fails_with_invalid_amount(self):
        user_service.create_user(
            self.valid_user.username, self.valid_user.password, self.valid_user.password)
        user_service.login(
            self.valid_user.username, self.valid_user.password)

        with self.assertRaises(InvalidExpenseError) as context:
            expense_service.add_expense(
                self.expense.description, "invalid", self.expense.date, self.valid_user.username)
        self.assertEqual(str(context.exception),
                         "Amount must be a valid number!")

    def test_update_expense_with_valid_data_works(self):
        user_service.create_user(
            self.valid_user.username, self.valid_user.password, self.valid_user.password)
        user_service.login(
            self.valid_user.username, self.valid_user.password)

        expense_service.add_expense(
            "car", 2000, "2025-04-08", self.valid_user.username)
        expenses = expense_repository.get_expenses_by_user(
            self.valid_user.username)
        self.assertEqual(len(expenses), 1)
        expense_id = expenses[0].expense_id

        expense_service.update_expense(expense_id, "bike", 1500, "2025-05-01")

        updated_expenses = expense_repository.get_expenses_by_user(
            self.valid_user.username)
        self.assertEqual(len(updated_expenses), 1)
        self.assertEqual(updated_expenses[0].description, "bike")
        self.assertEqual(updated_expenses[0].amount, 1500)
        self.assertEqual(updated_expenses[0].date, "2025-05-01")

    def test_update_expense_fails_with_invalid_amount(self):
        user_service.create_user(
            self.valid_user.username, self.valid_user.password, self.valid_user.password)
        user_service.login(
            self.valid_user.username, self.valid_user.password)

        with self.assertRaises(InvalidExpenseError) as context:
            expense_service.update_expense(1, "car", "invalid", "2025-04-08")
        self.assertEqual(str(context.exception),
                         "Amount must be a valid number!")

    def test_update_expense_fails_with_non_positive_amount(self):
        user_service.create_user(
            self.valid_user.username, self.valid_user.password, self.valid_user.password)
        user_service.login(
            self.valid_user.username, self.valid_user.password)

        with self.assertRaises(InvalidExpenseError) as context:
            expense_service.update_expense(1, "car", 0, "2025-04-08")
        self.assertEqual(str(context.exception),
                         "Amount must be greater than zero!")

        with self.assertRaises(InvalidExpenseError) as context:
            expense_service.update_expense(1, "car", -100, "2025-04-08")
        self.assertEqual(str(context.exception),
                         "Amount must be greater than zero!")

    def test_update_expense_fails_with_missing_fields(self):
        user_service.create_user(
            self.valid_user.username, self.valid_user.password, self.valid_user.password)
        user_service.login(
            self.valid_user.username, self.valid_user.password)

        with self.assertRaises(InvalidExpenseError) as context:
            expense_service.update_expense(1, "", 2000, "2025-04-08")
        self.assertEqual(str(context.exception), "All fields are required!")

        with self.assertRaises(InvalidExpenseError) as context:
            expense_service.update_expense(1, "car", None, "2025-04-08")
        self.assertEqual(str(context.exception), "All fields are required!")

        with self.assertRaises(InvalidExpenseError) as context:
            expense_service.update_expense(1, "car", "", "2025-04-08")
        self.assertEqual(str(context.exception), "All fields are required!")

        with self.assertRaises(InvalidExpenseError) as context:
            expense_service.update_expense(1, "car", 2000, "")
        self.assertEqual(str(context.exception), "All fields are required!")
