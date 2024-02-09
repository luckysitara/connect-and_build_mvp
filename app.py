from flask import Flask, render_template
from server import DatabaseConnector

app = Flask(__name__)
db_connector = DatabaseConnector()  # Assuming your server.py provides a class for database connection

@app.route('/')
def index():
    # Assuming you have a method in server.py to fetch data from MySQL
    data = db_connector.fetch_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

