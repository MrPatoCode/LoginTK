import sqlite3

class Connect:
    def __init__(self):
        self.name_data = "db/data.db"

    def connection(self):
        try:
            my_connection = sqlite3.connect(self.name_data)
            self.r = True
        except Exception as e:
            self.r = False
            print(e)
            
        return my_connection

    def verify(self):
        self.connection()
        return self.r       