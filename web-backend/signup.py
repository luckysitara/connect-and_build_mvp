from flask import Blueprint, render_template, redirect, url_for, flash
from form import SignupForm
from server import DatabaseConnector

signup_bp = Blueprint('signup', __name__)
db_connector = DatabaseConnector()

@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup_route():
    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('signup.signup_route'))
        if db_connector.user_exists(email):
            flash('User already exists', 'error')
            return redirect(url_for('signup.signup_route'))
        db_connector.create_user(email, password)
        return redirect(url_for('login.login_route'))
    return render_template('signup.html', form=form)

