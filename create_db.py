from sql_utilis import create_db, execute_sql

def start():
    while True:
        x = input(f"Co chcesz zrobić [Z - założyć bazę dznych], [P - pracować na bazie danych] ? ")
        if x.upper() == "Z":
            db = input(f"Podaj nazwę bazy danych: ")
            create_db(db)
        elif x.upper() == "P":
            db = input(f"Podaj bazę w której chcesz działać: ")
            command = input(f"Podaj komendę SQL: ")
            execute_sql(command, db)
        else:
            print(f"{x} nie jest dozwolone, musisz wybrać Z lub P!")

#ZAKŁĄDAMY BAZĘ message_db
#
#KOMENDY SQL do P:
# CREATE TABLE users (id serial PRIMARY KEY, username varchar(255) UNIQUE, hashed_password varchar(80));
# CREATE TABLE messages (id serial PRIMARY KEY, from_id int REFERENCES users(id) ON DELETE CASCADE, to_id int REFERENCES users(id) ON DELETE CASCADE, creation_date timestamp DEFAULT current_timestamp, text varchar(255));





if __name__ == "__main__":
    start()

