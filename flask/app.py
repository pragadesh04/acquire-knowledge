from flask import Flask, request, render_template, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hi bro</h1>"

@app.route('/contact', methods = ['get', 'post'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
    return render_template("contact.html",name=name, message=message)

if __name__ == "__main__":
    app.run(debug=True)