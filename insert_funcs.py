import sqlite3

#data - список кортежей из одного элемента
def insert_sents(data):
    try:
        con = sqlite3.connect('sqlite_python.db')
        print("Подключен к SQLite")

        sqlite_insert_query = """INSERT INTO sentences
                                (sentence)
                                VALUES(?);"""
        with con:
            con.executemany(sqlite_insert_query, data)

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if (con):
            con.close()
            print("Соединение с SQLite закрыто")
    return

#data - список кортежей из двух элементов
def insert_word(data):
    try:
        con = sqlite3.connect('sqlite_python.db')
        print("Подключен к SQLite")

        sqlite_insert_query = """INSERT INTO morphemes
                                 (word, morphemes)
                                 VALUES(?, ?);"""
        with con:
            con.execute(sqlite_insert_query, data)

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if (con):
            con.close()
            print("Соединение с SQLite закрыто")
    return