from app import app
from app import r
from app.models import Message

from flask import render_template, request, redirect, url_for


@app.route("/")
def index():

    r.incr("hits")
    hits = int(r.get("hits"))

    return render_template("index.html", hits=hits)


@app.route("/guestbook", methods=["GET", "POST"])
def guestbook():

    messages = Message.objects()

    if request.method == "POST":
        
        Message(
            name=request.form.get("name"),
            message=request.form.get("message")
        ).save()

        return redirect(request.url)

    return render_template("guestbook.html", messages=messages)