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

    def user_exists(self, email):
        query = "SELECT * FROM user WHERE email = %s"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchone()
        return result is not None

    def create_user(self, email, password):
        query = "INSERT INTO user (email, password) VALUES (%s, %s)"
        self.cursor.execute(query, (email, password))
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

