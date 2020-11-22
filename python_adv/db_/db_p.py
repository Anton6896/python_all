import sqlite3
import pathlib

db_file = str(pathlib.Path(__file__).parent.absolute()) + "/mydb.db"


def create_db():
    # create and fill db sqlite3
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        cursor.execute("""
        create table if not exists persons(
            first_name varchar(30),
            last_name varchar(30),
            age int
        );
        """)

        cursor.execute("""
        insert into persons values("fname3", "lname3", 23),("fname4", "lname4", 43),("fname4", "lname4", 43);
        """)
    except:
        print("some connection problens")
    finally:
        connection.commit()
        connection.close()


def get_data():
    # get data from sqlite3
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM persons
            where last_name = "lname4";
            """
        )

        # return list of tupels=rows
        rows = cursor.fetchall()
        print(rows)

    finally:
        connection.commit()
        connection.close()


if __name__ == "__main__":
    # db_use()
    get_data()
