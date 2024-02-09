import os
from flask import Flask, render_template
from server import DatabaseConnector

app = Flask(__name__)
db_connector = DatabaseConnector()

@app.route('/')
def index():
    data = db_connector.fetch_data()
    template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'template', 'index.html'))
    return render_template(template_path, data=data)

if __name__ == '__main__':
    app.run(debug=True)

