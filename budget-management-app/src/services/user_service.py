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
    '''Käyttäjiin liittyvästä sovelluslogiikasta huolehtiva luokka'''

    def __init__(self, repository):
        '''Luokan konstruktori, joka luo uuden käyttäjiin liittyvän sovelluslogiikan palvelun

            Args:
                repository: Olio, jolla on UserRepository-luokkaa vastaavat metodit
        '''
        self._user = None
        self._user_repository = repository

    def set_budget(self, username, budget):
        ''' Asettaa käyttälle uuden budjetin

            Args:
                username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta
                budget: Desimaaliarvo, joka kuvaa käyttäjän kuukausibudjettia
        '''
        try:
            monthly_budget = float(budget)
        except ValueError as exc:
            raise ValueError("Budget must be a valid number!") from exc

        if monthly_budget <= 0:
            raise ValueError("Budget must be a positive number!")

        self._user_repository.update_budget(username, monthly_budget)
        self._user.monthly_budget = monthly_budget

    def get_current_budget(self):
        ''' Funktio, joka palauttaa käyttäjän nykyisen budjetin

        Returns:
            Palauttaa käyttäjän nykyisen budjetin
        '''
        if self._user.monthly_budget is None:
            return None
        expenses = expense_repository.get_expenses_by_user(self._user.username)
        total_expenses = sum(expense.amount for expense in expenses)
        return round(self._user.monthly_budget - total_expenses, 2)

    def create_user(self, username: str, password: str, password_confirm: str):
        ''' Funktio, joka luo uuden käyttäjän

        Args: 
            username: Merkkijonoarvo, kuvaa käyttäjän käyttäjätunnusta ohjelmaan
            password: Merkkijonoarvo, kuvaa käyttäjän salasanaa ohjelmaan
            password_confirm: Merkkijonoarvo, kuvaa käyttäjän salasanaa ohjelmaan

        Returns:
            Palauttaa User-olion
        '''
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
        ''' Funktio, joka huolehtii käyttäjän kirjautumisesta

        Args: 
            username: Merkkijonoarvo, kuvaa käyttäjän käyttäjätunnusta ohjelmaan
            password: Merkkijonoarvo, kuvaa käyttäjän salasanaa ohjelmaan

        Returns:
            Palauttaa User-olion
        '''
        user = self._user_repository.get_user_by_name(username)

        if not user or not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user
        return user

    def logout(self):
        '''Funktio, joka huolehtii käyttäjän uloskirjautumisesta järjestelmästä'''
        self._user = None


user_service = UserService(user_repository)
