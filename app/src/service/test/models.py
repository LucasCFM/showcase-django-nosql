from mongoengine import Document, EmbeddedDocument, fields
from uuid import uuid4

ACTIVE_QUESTIONS_STATUS = 'active'
INACTIVE_QUESTIONS_STATUS = 'inactive'


class QuestionAnswer(EmbeddedDocument):
    id = fields.UUIDField(primary=True, default=lambda: uuid4(), binary=False)
    text = fields.StringField(required=True)


class Question(EmbeddedDocument):
    id = fields.UUIDField(primary=True, default=lambda: uuid4(), binary=False)
    text = fields.StringField(required=True)
    answers = fields.ListField(fields.EmbeddedDocumentField(QuestionAnswer), required=False)
    correctAnswers = fields.ListField(fields.StringField(), required=True)
    userAnswer = fields.ListField(fields.StringField(), required=False)
    status = fields.StringField(required=True)
    order = fields.IntField(required=True)


class Test(Document):
    name = fields.StringField(required=True)
    summary = fields.StringField(required=True)
    type = fields.IntField(required=True)
    duration = fields.IntField(required=True)
    level = fields.StringField(required=True)
    audience = fields.StringField(required=True)
    language = fields.StringField(required=True)
    skills = fields.ListField(fields.StringField())
    questions = fields.ListField(fields.EmbeddedDocumentField(Question), required=True)
