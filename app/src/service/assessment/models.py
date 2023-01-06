from uuid import uuid4
from service.tests.models import Test
from mongoengine import Document, fields


class Assessment(Document):
    id = fields.UUIDField(required=True, default=lambda: uuid4(), binary=False)
    name = fields.StringField(required=True)
    summary = fields.StringField(required=True)
    duration = fields.IntField(required=True)
    level = fields.StringField(required=True)
    tests = fields.ListField(fields.EmbeddedDocumentField(Test), required=True)
