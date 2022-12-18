from marshmallow import Schema, fields, ValidationError, validates_schema

VALID_CMD = ('filter', 'map', 'unique', 'sort', 'limit', 'regex')


class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values, *args, **kwargs):
        if values['cmd'] not in VALID_CMD:
            raise ValidationError('invalid "cmd" value')


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
