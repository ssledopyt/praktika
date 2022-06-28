import sqlite3

try:
    sqlite_connection = sqlite3.connect('test.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к sqlite")

    sqlite_select_query = "SELECT sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("версия базы данных sqlite: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("соединение с sqlite закрыто")