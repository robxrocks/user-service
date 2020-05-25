from marshmallow import Schema, fields


class EmailSchema(Schema):
    mail = fields.Str()
