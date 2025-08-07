from marshmallow import Schema, fields

class ItemSchema(Schema):
    # dump_only => only used for returning data
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    price = fields.Float() # not required
    name = fields.Str()

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)