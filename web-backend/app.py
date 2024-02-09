import os
from flask import Flask, render_template, redirect
from server import DatabaseConnector

app = Flask(__name__)
db_connector = DatabaseConnector()

@app.route('/login', methods=['POST'])
def login_route():
    # Process login form data here
    # Example: check username and password, authenticate user
    return redirect(url_for('index'))  # Redirect to homepage after login

@app.route('/signup', methods=['POST'])
def signup_route():
    # Process signup form data here
    # Example: create new user account
    return redirect(url_for('index'))  # Redirect to homepage after signup

@app.route('/')
def index():
    # Render your index.html template here
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

