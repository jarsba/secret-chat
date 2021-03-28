from marshmallow import Schema, fields, ValidationError, pre_load

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    email = fields.Str()
    username = fields.Str()
