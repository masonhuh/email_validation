from flask_app import app
from flask import render_template, redirect, request, flash, session

from flask_app.models.user import User

@app.route('/')
def index():
    print('Home')
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def create_email():
    if not User.validate_user(request.form):
        return redirect('/')
    return redirect('/success')

@app.route('/success')
def get_emails():
    emails = User.get_emails()
    return render_template('emails.html', emails = emails)