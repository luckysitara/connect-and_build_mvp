
import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_wtf.csrf import CSRFProtect
from form import LoginForm, SignupForm
from server import DatabaseConnector


app = Flask(__name__)
app.secret_key = 'goANDaskTHEdevilINhell'
csrf = CSRFProtect(app)
db_connector = DatabaseConnector()


@app.route('/')
def index():
    # Render your index.html template here
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login_route():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Example: Perform authentication (check username and password)
        # Replace this with your authentication logic
        if db_connector.authenticate_user(email, password):
            # Authentication successful, redirect to homepage
            return redirect(url_for('index'))
        else:
            # Authentication failed, return an error message
            return "Invalid email or password"

    # If the request method is GET or form validation fails, render the login form template
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup_route():
    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        # Basic validation
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('signup_route'))

        # Example: Check if user already exists in the database
        if db_connector.user_exists(email):
            flash('User already exists', 'error')
            return redirect(url_for('signup_route'))

        # Create new user account
        db_connector.create_user(email, password)

        # Redirect to login page after signup
        return redirect(url_for('login_route'))  # Corrected redirection to the login route

    # If the request method is GET or form validation fails, render the signup form template
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)


