import logging
import sqlite3


def main():
    logging.basicConfig(level=logging.INFO)
    #connection = sqlite3.connect("4. Context Managers/application.db")
    # try:
    #     cursor = connection.cursor()
    #     cursor.execute("SELECT * FROM blogs")
    #     logging.info(cursor.fetchall())
    # finally:
    #     connection.close()

    # if we want to avoid the try finally
    with sqlite3.connect("4. Context Managers/application.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM bloggs")
        logging.info(cursor.fetchall())


if __name__ == "__main__":
    main()