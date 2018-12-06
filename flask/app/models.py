from mongoengine import Document, StringField


class Message(Document):
    name = StringField()
    message = StringField()