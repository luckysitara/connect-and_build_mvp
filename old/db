import mysql.connector

class DatabaseConnector:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connectAndBuild"
        )
        self.cursor = self.connection.cursor()

    def fetch_data(self):
        query = "SELECT * FROM user"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

