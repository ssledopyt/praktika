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

    def try_smth(self, table):
        self.cursor.execute(f"""
            PRAGMA table_info({table.name});""")
        return self.cursor.fetchall()

    def try_add_columns(self, table, **kwargs):
        try:
            for name_of_column, type_of_column in kwargs.items():
                self.cursor.execute(f"""
                    ALTER TABLE {table.name} ADD COLUMN
                    {name_of_column} {type_of_column};
                    """)
                self.connection.commit()
        except:
            pass

    def get_table_object(self, table, name_of_column, value_of_column):
        self.cursor.execute(f"""SELECT * FROM {table.name}
        WHERE {name_of_column} = {value_of_column};
        """)
        return self.cursor.fetchall()

    def create_table_object(self, table, *args):
        param = ""
        for i in args:
            if isinstance(i, str):
                param += "'" + str(i) + "'" + ','
            else:
                param += str(i) + ','
        param = param[:-1]
        self.cursor.execute(f"""
        INSERT INTO {table.name}({','.join(table.colums.keys())})
        VALUES ({param});
        """)
        self.connection.commit()
        return self.cursor.fetchall()

    def update_table_object(self, table, name_of_column, value_of_column, *args):
        for index, column in enumerate(list(table.colums.keys())[1:]):
            self.cursor.execute(f"""
            UPDATE {table.name} SET {column} = {args[index] if isinstance(args[index], int) 
            else "'" + args[index] +"'"} where {name_of_column} = {value_of_column};
            """)
            self.connection.commit()

    def delete_table_object(self,):

    def __delete__(self, instance):
        self.cursor.close()
        self.connection.close()
        super().__delete__(self, instance)

class Table:
    def __init__(self, name, datab):
        self.colums = {}
        self.datab = datab
        self.name = name
        self.datab.try_add_table(name)
        for column in self.datab.try_smth(self):
            self.colums[column[1]] = column[2]

    def add_colums(self, **kwargs):
        for name_of_column, type_of_column in kwargs.items():
            self.colums[name_of_column] = type_of_column
        self.datab.try_add_columns(self, **kwargs)
        print(kwargs)

    def create_objects(self, *args):
        self.datab.create_table_object(self, *args)

    def try_smth(self):
        self.datab.try_smth(self)

db = Database('test')
anims = Table('anims', db)
columns = {'name': 'TEXT'}
anims.add_colums(**columns)
anims.try_smth()
anims.create_objects(1, 'alica')
print(anims.colums)
