import sqlite3

try:
    sqlite_connection = sqlite3.connect('test.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к sqlite")

    cursor.execute("""
    SELECT * FROM test
    """)
    objects = cursor.fetchall()
    for object in objects:
        for value in object:
            print(value)

    sqlite_connection.commit()

    cursor.close()

except sqlite3.Error as error:
    print("ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("соединение с sqlite закрыто")