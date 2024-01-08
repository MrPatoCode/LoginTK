from db.connectionDb import Connect

class OperationsDb:
    connect = Connect()
    my_connection = connect.connection()
    cursor = my_connection.cursor()

    def selectUser(self, user, passwd):
        self.cursor.execute("SELECT user, password FROM Users WHERE user = ?", (user,))
        data = self.cursor.fetchall()
        for user, passwd in data:
            data =(user, passwd)
        
        self.my_connection.commit()
        return data

    def insertRegister(self, user, passwd):
        self.cursor.execute("INSERT INTO Users (user, password) VALUES (?, ?)", (user, passwd,))
        self.my_connection.commit()
