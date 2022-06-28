import sqlite3


class Database:
    def __init__(self, name):
        self.connection = sqlite3.connect(f'{name}.db')

    def inspect(self):
        print(self.__dict__)

    def __delete__(self, instance):
        self.connection.close()
        super().__delete__(self, instance)

        
db = Database('test')
db.inspect()