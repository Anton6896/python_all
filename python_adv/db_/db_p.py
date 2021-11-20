import sqlite3
import pathlib


db_file = str(pathlib.Path(__file__).parent.absolute()) + "/mydb.db"


def create_db():
    # create and fill db sqlite3
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        #  execute and fill the database one by one ! cant do all in once
        # the id is auto increment called by "rowid"

        # cursor.execute(
        #     """
        #     create table if not exists persons(
        #         id INTEGER PRIMARY KEY,
        #         first_name varchar(30),
        #         last_name varchar(30),
        #         age int);
        #     """
        # )

        cursor.execute(
            """
            INSERT INTO persons (first_name, last_name, age)
            VALUES ("name7", "lname7", 56);
            """
        )
    except:
        print("some connection problens")
    finally:
        connection.commit()
        connection.close()


def get_data():
    connection = None
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


class Person:

    def __init__(self, id_=-1, fname_="", lname_="", age_=0) -> None:
        self.id = id_
        self.fname = fname_
        self.lname = lname_
        self.age = age_

    def __str__(self) -> str:
        return self.fname + " " + self.lname

    def load_person(self, id_):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

        # load and create person from db by id
        self.cursor.execute(
            f"""
            SELECT * FROM persons
            where rowid = {id_};
            """
        )

        result = self.cursor.fetchone()

        self.id = id_
        self.fname = result[1]
        self.lname = result[2]
        self.age = result[3]

        self.connection.commit()
        self.connection.close()

        return self

    def insert_person(self):
        try:
            self.connection = sqlite3.connect(db_file)
            self.cursor = self.connection.cursor()

            self.cursor.execute(
                f""" 
                INSERT INTO persons (first_name, last_name, age)
                VALUES ("{self.fname}","{self.lname}","{self.age}");
                """
            )
        except:
            print("some connection problens")

        finally:
            self.connection.commit()
            self.connection.close()
        return self

    def show_all(self):
        try:
            self.connection = sqlite3.connect(db_file)
            self.cursor = self.connection.cursor()

            # some how cant insert the data from modified string !
            self.cursor.execute(
                """
                SELECT * FROM persons;
                """
            )
            result = self.cursor.fetchall()
            print(result)

        except:
            print("some connection problens")

        finally:
            self.connection.commit()
            self.connection.close()
        
        return self


if __name__ == "__main__":
    # create_db()
    get_data()
    # p1 = Person().load_person(2)
    # print(p1)
    #
    # p2 = Person(10, "person10", "lname10", 56).insert_person()
    # p1.show_all()

