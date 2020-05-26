from marshmallow import Schema, fields, validate


class EmailSchema(Schema):
    mail = fields.Str(required=True, validate=validate.Length(min=7))
