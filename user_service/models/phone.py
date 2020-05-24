from db import db
from flask_restful import fields
from swagger import swagger


@swagger.model
class Phone(db.Model):
    resource_fields = {
        'number': fields.String()
    }
    __tablename__ = 'phone'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User')

    def __init__(self, number, user_id):
        self.number = number
        self.user_id = user_id

    def json(self):
        return {'id': self.id,
                'number': self.number
                }

    @classmethod
    def get_by_id(cls, phone_id):
        return cls.query.filter_by(id=phone_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
