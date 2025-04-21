from entities.expense import Expense
from repositories.expense_repository import expense_repository


class InvalidExpenseError(Exception):
    pass


class ExpenseService:
    ''' Luokka, joka huolehtii kuluihin liittyvästä sovelluslogiikasta'''

    def __init__(self, expense_repository):
        '''Luokan konstruktori, joka luo uuden kuluihin liittyvän sovelluslogiikan palvelun

            Args:
                expense_repository: Olio, jolla on ExpenseRepository-luokkaa vastaavat metodit
        '''
        self._expense_repository = expense_repository

    def add_expense(self, description, amount, date, username):
        ''' Funktio, joka luo uuden kulun

            Args:
                description: Merkkijonoarvo, joka on kuvaus kulusta
                amount: Desimaaliarvo, joka määrittelee kulun summan arvon
                date: Merkkijonoarvo, joka määrittelee kulun päivämäärän
                username: Merkkijonoarvo, joka kuvaa käyttäjän tunnusta
        '''
        if not description or amount is None or amount == "" or not date:
            raise InvalidExpenseError("All fields are required!")

        try:
            amount = float(amount)
        except ValueError as exc:
            raise InvalidExpenseError(
                "Amount must be a valid number!") from exc

        if amount <= 0:
            raise InvalidExpenseError("Amount must be greater than zero!")

        expense = Expense(description=description, amount=amount, date=date)
        self._expense_repository.create_expense(expense, username)

    def update_expense(self, expense_id, description, amount, date):
        ''' Funktio, joka muokkaa olemassaolevaa kulua

            Args:
                description: Merkkijonoarvo, joka on kuvaus kulusta
                amount: Desimaaliarvo, joka määrittelee kulun summan arvon
                date: Merkkijonoarvo, joka määrittelee kulun päivämäärän
                expense_id: Kokonaislukuarvo, joka kuvaa kulun id:tä
        '''
        if not description or amount is None or amount == "" or not date:
            raise InvalidExpenseError("All fields are required!")

        try:
            amount = float(amount)
        except ValueError as exc:
            raise InvalidExpenseError(
                "Amount must be a valid number!") from exc
        if amount <= 0:
            raise InvalidExpenseError("Amount must be greater than zero!")

        expense_repository.update_expense(
            expense_id, description, amount, date)

    def delete_expense(self, expense_id):
        ''' Funktio, joka poistaa olemassaolevan kulun'''
        expense_repository.delete_expense(expense_id)

    def get_expenses_by_user(self, username):
        ''' Funktio, joka palauttaa käyttäjän kulut listana Expense-olioita

            Args:
                username: Merkkijonoarvo, joka kuvaa käyttäjän tunnusta

            Returns:
                palauttaa listan käyttäjän kuluista Expense-olioina
        '''
        return expense_repository.get_expenses_by_user(username)


expense_service = ExpenseService(expense_repository)
