from psycopg2 import connect, ProgrammingError, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"

def execute_sql(sql_code, db):
    """
    Run given sql code with psycopg2.

    :param str sql_code: sql code to run
    :param str db: name of db,

    :rtype: list
    :return: data from psycobg2 cursor as a list (can be None) if nothing to fetch.
    """

    try:
        cnx = connect(user=USER, password=PASSWORD, host=HOST, database=db)
        cursor = cnx.cursor()
        cursor.execute(sql_code)
        cnx.commit()
    #    result = [item for item in cursor]
        if cursor.description:
            result = [item for item in cursor]
        else:
            result = None
    except ProgrammingError as exc:
        print(f"Błąd! {exc}")
    except DuplicateTable:
        print(f"Tablica juz istnieje!")
    except OperationalError as exc:
        print(f"Błąd! {exc}")
    else:
        cursor.close()
        cnx.close()
        return result

def create_db (db):
    """
    Program is creating database.

    :param str db: name of db,
    """
    sql_code = f"CREATE DATABASE {db};"
    try:
        cnx = connect(user=USER, password=PASSWORD, host=HOST)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute(sql_code)
        print(f"Baza {db} została założona.")
    except DuplicateDatabase:
        print(f"Baza {db} juz istnieje!")
    except OperationalError:
        print("Błąd!")
    else:
        cursor.close()
        cnx.close()