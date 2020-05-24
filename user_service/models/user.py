from db import db
from swagger import swagger

from models.email import Email
from models.phone import Phone
import json

from flask_restful import fields


@swagger.model
# @swagger.nested(
#     emails=Email.__name__,
#     phones=Phone.__name__)
class User(db.Model):
    resource_fields = {
        'lastName': fields.String(),
        'firstName': fields.String(),
        'emails': fields.List(fields.Nested(Email.resource_fields)),
        'phones': fields.List(fields.Nested(Phone.resource_fields))
    }
    required = ['lastName', 'firstName', 'emails', 'phones']

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(50))
    firstName = db.Column(db.String(50))

    emails = db.relationship('Email', lazy='dynamic', cascade="all, delete", single_parent=True)
    phones = db.relationship('Phone', lazy='dynamic', cascade="all, delete", single_parent=True)

    def __init__(self, lastName, firstName, emails, phone_numbers):
        self.lastName = lastName
        self.firstName = firstName

        for email in list(emails):
            email = json.loads(email.replace("\'", "\""))
            self.emails.append(Email(email['mail'], self.id))

        for phone in list(phone_numbers):
            phone = json.loads(phone.replace("\'", "\""))
            print(phone['number'])
            self.phones.append(Phone(phone['number'], self.id))

    def json(self):
        return {'id': self.id,
                'lastName': self.lastName,
                'firstName': self.firstName,
                'emails': [email.json() for email in self.emails.all()],
                'phoneNumbers': [phone.json() for phone in self.phones.all()]
                }

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def get_by_name(cls, last_name, first_name):
        return cls.query.filter(cls.lastName.ilike(last_name), cls.firstName.ilike(first_name)).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
