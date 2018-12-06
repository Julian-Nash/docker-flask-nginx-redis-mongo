from app import app
from app import r
from app.models import Message

from flask import render_template
from mongoengine import NotUniqueError


@app.route("/")
def index():

    r.incr("hits")
    hits = int(r.get("hits"))

    try:
        Message(
            name="Julian Nash", 
            message="And this message was saved and pulled from the database."
        ).save()
    except NotUniqueError:
        pass

    message = Message.objects().get()

    return render_template("index.html", hits=hits, message=message)