from app import app
from app import r
from app.models import Message

from flask import render_template


@app.route("/")
def index():

    r.incr("hits")
    hits = int(r.get("hits"))

    return render_template("index.html", hits=hits)