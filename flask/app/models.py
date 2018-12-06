from mongoengine import Document, StringField


class Message(Document):
    name = StringField(unique=True)
    message = StringField()