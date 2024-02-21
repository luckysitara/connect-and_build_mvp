from flask import Flask, render_template
from login import login_bp
from signup import signup_bp

app = Flask(__name__)
app.secret_key = 'goANDaskTHEdevilINhell'

app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

