from flask import render_template

from app import app
from app.models.forms import LoginForm


@app.route("/index/<user>")
@app.route("/")
def index(user=None):
    if user:
        return render_template("index.html", user=user.title())
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    return render_template("login.html", form=form)


@app.route("/test")
@app.route("/test/<name>")
def test(name=None):
    if name:
        name = name.title()
        return f"Olá! {name}"
    return "Olá, usuário!"
