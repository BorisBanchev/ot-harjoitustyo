from entities.expense import Expense
from db.database_connection import get_database_connection


class ExpenseRepository:
    ''' Luokka, joka huolehtii käyttäjän kuluun liittyvistä tietokantaoperaatioista

    Attributes:
        db: Polku tiedostoon, johon kulut tallennetaan
    '''

    def __init__(self, db):
        ''' Luokan konstruktori

        Args: 
            db: Polku tiedostoon, johon kulut tallennetaan
        '''
        self._db = db

    def create_expense(self, expense: Expense, username: str):
        ''' Funktio, joka tallentaa uuden kulun tietokantaan

        Args:
            expense: Expense-luokan olio, joka esittää yksittäistä kulua
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta
        '''
        cursor = self._db.cursor()
        cursor.execute('''
            INSERT INTO expenses (description, amount, date, username)
            VALUES (?, ?, ?, ?)
        ''', (expense.description, expense.amount, expense.date, username))
        self._db.commit()

    def get_expenses_by_user(self, username: str):
        ''' Funktio, joka hakee tietokannasta käyttäjän kulut ja palauttaa ne listana Expense-olioita

        Args: 
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta

        Returns:
            Palauttaa listan Expense-olioita eli käyttäjän kulut
        '''
        cursor = self._db.cursor()
        cursor.execute('''
            SELECT * FROM expenses WHERE username = ?
        ''', (username, ))
        rows = cursor.fetchall()
        return [Expense(row["description"], row["amount"], row["date"], row["id"]) for row in rows]

    def update_expense(self, expense_id, description, amount, date):
        ''' Funktio, joka päivittää tietokantaan kulun uudet kentät

        Args:
            expense_id: Kokonaislukuarvo, joka kertoo kulun id:n
            description: Merkkijonoarvo, joka on kuvaus kulusta
            amount: Desimaaliarvo, joka määrittelee kulun summan arvon
            date: Merkkijonoarvo, joka määrittelee kulun päivämäärän

        '''
        cursor = self._db.cursor()
        cursor.execute('''
            UPDATE expenses
            SET description = ?, amount = ?, date = ?
            WHERE id = ?
        ''', (description, amount, date, expense_id))
        self._db.commit()

    def delete_expense(self, expense_id: int):
        ''' Funktio, joka poistaa tietokannasta käyttäjän kulun

        Args:
            expense_id: Kokonaislukuarvo, joka kertoo kulun id:n

        '''
        cursor = self._db.cursor()
        cursor.execute('''
            DELETE FROM expenses WHERE id = ?
        ''', (expense_id, ))
        self._db.commit()

    def delete_all_expenses(self):
        ''' Funktio, joka poistaa kaikki kulut tietokannasta (käytetään testeissä)'''
        cursor = self._db.cursor()
        cursor.execute("DELETE FROM expenses")
        self._db.commit()


expense_repository = ExpenseRepository(get_database_connection())
