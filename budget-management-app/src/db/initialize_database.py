from db.database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS expenses;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            monthly_budget INTEGER
        );
    ''')

    cursor.execute('''
        CREATE TABLE expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            username TEXT NOT NULL,
            FOREIGN KEY (username) REFERENCES users (username)
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
