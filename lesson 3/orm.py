import sqlite3


class Database:
    def __init__(self, name):
        self.connection = sqlite3.connect(f'{name}.db')
        self.cursor = self.connection.cursor()


    def inspect(self):
        print(self.__dict__)

    def try_add_table(self, name):
        try:
            self.cursor.execute(f"""
                create table {name} (
                id INTEGER PRIMARY KEY);
                """)
        except:
            pass

    def try_add_columns(self, table, **kwargs):
        try:
            self.cursor.execute(f"""
                ALERT TABLE {table} ADD COLUMN(
                name NOT NULL KEY);
                """)
        except:
            pass

    def __delete__(self, instance):
        self.cursor.close()
        self.connection.close()
        super().__delete__(self, instance)

class Table:
    def __init__(self, name, datab):
        self.datab = datab
        self.name = name

    def add_columns(self, **kwargs):
        print(kwargs)


db = Database('test')
anims = Table('anims', db)
anims.add_columns()
