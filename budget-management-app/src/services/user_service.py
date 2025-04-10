import bcrypt
from entities.user import User
from repositories.user_repository import user_repository
from repositories.expense_repository import expense_repository


class UsernameExistsError(Exception):
    pass


class PasswordsNotMatchingError(Exception):
    pass


class InvalidPasswordOrUsernameError(Exception):
    pass


class EmptyUsernameOrPasswordError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user = None
        self._user_repository = user_repository

    def set_budget(self, username, budget):
        try:
            monthly_budget = int(budget)
        except ValueError:
            raise ValueError("Budget must be a valid number!")

        if monthly_budget <= 0:
            raise ValueError("Budget must be a positive number!")

        self._user_repository.update_budget(username, monthly_budget)
        self._user.monthly_budget = monthly_budget

    def get_current_budget(self):
        if self._user.monthly_budget is None:
            return None
        expenses = expense_repository.get_expenses_by_user(self._user.username)
        total_expenses = sum(expense.amount for expense in expenses)
        return self._user.monthly_budget - total_expenses

    def create_user(self, username: str, password: str, password_confirm: str):

        existing_user = self._user_repository.get_user_by_name(username)

        if len(username) == 0 or len(password) == 0:
            raise EmptyUsernameOrPasswordError(
                "Username and password must not be empty values!")
        if existing_user:
            raise UsernameExistsError("Username {username} already exists!")
        if password != password_confirm:
            raise PasswordsNotMatchingError("Passwords do not match!")
        if len(username) < 4 or len(password) < 4:
            raise InvalidPasswordOrUsernameError(
                "Password and username must have legth of at least 4!")

        user = self._user_repository.create_user(User(username, password))
        self._user = user
        return user

    def login(self, username: str, password: str):
        user = self._user_repository.get_user_by_name(username)

        if not user or not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user
        return user

    def logout(self):
        self._user = None

user_service = UserService(user_repository)
