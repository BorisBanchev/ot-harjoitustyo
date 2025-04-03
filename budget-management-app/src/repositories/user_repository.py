from entities.user import User
from db.database_connection import get_database_connection
import bcrypt


class UserRepository:
    def __init__(self, db):
        self._db = db

    def get_all_users(self):
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        return [User(row["username"], row["password"], row["monthly_budget"]) for row in rows]

    def get_user_by_name(self, username: str):
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()

        if row:
            return User(row["username"], row["password"], row["monthly_budget"])
        return None

    def create_user(self, user: User):
        cursor = self._db.cursor()
        hashed_password = bcrypt.hashpw(
            user.password.encode("utf-8"), bcrypt.gensalt())
        cursor.execute("INSERT INTO users (username, password) VALUES (?,?)",
                       (user.username, hashed_password.decode("utf-8")))

        self._db.commit()

        return user

    def delete_all_users(self):
        cursor = self._db.cursor()
        cursor.execute("DELETE FROM users")
        self._db.commit()

    def update_budget(self, username, budget):
        monthly_budget = budget
        cursor = self._db.cursor()
        cursor.execute('''
            UPDATE users
            SET monthly_budget = ?
            WHERE username = ?
        ''', (monthly_budget, username))
        self._db.commit()


user_repository = UserRepository(get_database_connection())
