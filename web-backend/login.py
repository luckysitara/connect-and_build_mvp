from flask import Blueprint, render_template, redirect, url_for, flash
from form import LoginForm
from server import DatabaseConnector

login_bp = Blueprint('login', __name__)
db_connector = DatabaseConnector()

@login_bp.route('/login', methods=['GET', 'POST'])
def login_route():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if db_connector.authenticate_user(email, password):
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'error')
    return render_template('login.html', form=form)

