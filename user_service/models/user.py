from db import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(50))
    firstName = db.Column(db.String(50))

    def __init__(self, lastName, firstName):
        self.lastName = lastName
        self.firstName = firstName

    def json(self):
        return {'id': self.id,
                'lastName': self.lastName,
                'firsName': self.firstName
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
