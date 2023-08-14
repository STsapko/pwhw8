from mongoengine import Document, StringField, BooleanField

class User(Document):
    fullname = StringField(required = True)
    email = StringField(required = True)
    sent = BooleanField(default=False)
    