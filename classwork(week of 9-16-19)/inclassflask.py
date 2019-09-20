from flask import Flask, render_template, flash, redirect, url_for, request
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, required
from flask_wtf import FlaskForm
app = Flask(__name__)

class lazyForm(FlaskForm):
    submit = SubmitField('Sign In')


@app.route("/")
def hello_world():
    print(__name__)
    return("no habloe queso")

if (__name__ == "__main__"):
    app.debug = True
    app.run()

@app.route("/hell")
def test():
    print("hiya")
    return("blah")

@app.route("/magic")
def yu():
    return("nothing")