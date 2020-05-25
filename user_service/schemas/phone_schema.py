from marshmallow import Schema, fields


class PhoneSchema(Schema):
    number = fields.Str()
