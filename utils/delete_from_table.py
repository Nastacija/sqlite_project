import sqlite3

try:
        con = sqlite3.connect('sqlite_python.db')
        print("Подключен к SQLite")

        sqlite_insert_query = """DELETE FROM morphemes WHERE word='мама'"""
        with con:
            con.execute(sqlite_insert_query)

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if (con):
        con.close()
        print("Соединение с SQLite закрыто")