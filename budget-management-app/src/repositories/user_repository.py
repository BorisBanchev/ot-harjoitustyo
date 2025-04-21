import bcrypt
from entities.user import User
from db.database_connection import get_database_connection


class UserRepository:
    ''' Luokka, joka huolehtii käyttäjiin liittyvistä tietokantaoperaatioista

    Attributes:
        db: Polku tiedostoon, johon kulut tallennetaan
    '''

    def __init__(self, db):
        ''' Luokan konstruktori

        Args: 
            db: Polku tiedostoon, johon kulut tallennetaan
        '''
        self._db = db

    def get_all_users(self):
        ''' Funktio, joka hakee tietokannasta käyttäjät ja palauttaa ne listana User-olioita

        Returns:
            Palauttaa listan User-olioita eli kaikki käyttäjät
        '''
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        return [User(row["username"], row["password"], row["monthly_budget"]) for row in rows]

    def get_user_by_name(self, username: str):
        ''' Funktio, joka hakee tietokannasta yksittäisen käyttäjän

        Args: 
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta

        Returns:
            Palauttaa yksittäisen User-olion eli käyttäjän
        '''
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()

        if row:
            return User(row["username"], row["password"], row["monthly_budget"])
        return None

    def create_user(self, user: User):
        ''' Funktio, joka luo uuden käyttäjän tietokantaan

        Args: 
            user: User-olio, joka kuvaa käyttäjää järjestelmässä

        Returns:
            Palauttaa User-olion
        '''
        cursor = self._db.cursor()
        hashed_password = bcrypt.hashpw(
            user.password.encode("utf-8"), bcrypt.gensalt())
        cursor.execute("INSERT INTO users (username, password) VALUES (?,?)",
                       (user.username, hashed_password.decode("utf-8")))

        self._db.commit()

        return user

    def delete_all_users(self):
        ''' Funktio, joka poistaa tietokannasta kaikki käyttäjät (käytetään testauksessa)
        '''
        cursor = self._db.cursor()
        cursor.execute("DELETE FROM users")
        self._db.commit()

    def update_budget(self, username, budget):
        ''' Funktio, joka asettaa käyttäjälle budjetin

        Args: 
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta
            budget: Desimaaliarvo, joka kuvaa käyttäjän kuukausibudjettia
        '''
        monthly_budget = budget
        cursor = self._db.cursor()
        cursor.execute('''
            UPDATE users
            SET monthly_budget = ?
            WHERE username = ?
        ''', (monthly_budget, username))
        self._db.commit()


user_repository = UserRepository(get_database_connection())
