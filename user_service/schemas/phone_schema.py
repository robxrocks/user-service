from marshmallow import Schema, fields, validate


class PhoneSchema(Schema):
    number = fields.Str(required=True, validate=validate.Length(min=11))
