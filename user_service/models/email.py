from db import db


class Email(db.Model):
    __tablename__ = 'email'

    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User')

    def __init__(self, mail, user_id):
        self.mail = mail
        self.user_id = user_id

    def json(self):
        return {'id': self.id,
                'mail': self.mail,
                'user_id': self.user_id
                }

    @classmethod
    def get_by_id(cls, email_id):
        return cls.query.filter_by(id=email_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
