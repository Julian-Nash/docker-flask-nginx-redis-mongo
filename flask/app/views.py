from app import app
from app.models import Message

from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")