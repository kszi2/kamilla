import sqlite3

from bot import debugLogger


def init_table():
    conn = sqlite3.connect('runtime/data.db')
    cursor = conn.cursor()
    # Initialize DB
    cursor.execute('''CREATE TABLE IF NOT EXISTS openings
                        (nextOpeningDate datetime NOT NULL,
                        circleName text NOT NULL,
                        PRIMARY KEY(nextOpeningDate, circleName) )''')
    cursor.close()


def insert_opening(opening):
    name = opening.circleName
    date = opening.nextOpeningDate

    conn = sqlite3.connect('runtime/data.db')
    cursor = conn.cursor()

    try:
        cursor.execute(f"INSERT INTO openings VALUES('{date}', '{name}')")
    except sqlite3.IntegrityError:
        debugLogger.log(f"Opening with name '{name}' and nextOpeningDate '{date}' already exists")

    cursor.connection.commit()
    cursor.close()


def select_all_openings():
    conn = sqlite3.connect('runtime/data.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM openings')
    openings = cursor.fetchall()

    cursor.close()
    return openings