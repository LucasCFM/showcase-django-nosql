from django.test import TestCase
from service.settings import MONGO_ENGINE, MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASSWORD, MONGO_DATABASE
from service.test.models import Test
from service.storage.mongo.mongo_client import MongoClient
from os import getenv
from tests.fake_data import COMPLETE_TEST
from service.test.utils import extract_questions_from_list


class TestTestCase(TestCase):
    def setUp(self):
        MongoClient.connect(MONGO_ENGINE, MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASSWORD, MONGO_DATABASE)

    def test_inset_test_on_db(self):
        """Inserted tests can be retrieved having the same data"""
        t = Test(
            name = COMPLETE_TEST.get('name'),
            summary = COMPLETE_TEST.get('summary'),
            type = COMPLETE_TEST.get('type'),
            duration = COMPLETE_TEST.get('duration'),
            level = COMPLETE_TEST.get('level'),
            audience = COMPLETE_TEST.get('audience'),
            language = COMPLETE_TEST.get('language'),
            skills = COMPLETE_TEST.get('skills')
        )
        t.questions = extract_questions_from_list(COMPLETE_TEST.get('questions'))
        t.save()

        saved_test = Test.objects().first()
        self.assertEqual(saved_test.name, t.name)
