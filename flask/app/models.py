from mongoengine import Document, StringField, DateTimeField
import datetime


class Message(Document):
    name = StringField()
    message = StringField()
    date = DateTimeField(default=datetime.datetime.utcnow)

    meta = {
        "ordering": [
            "-date"
        ]
    }