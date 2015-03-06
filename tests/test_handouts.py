from django.test import TestCase, Client
from django.utils import timezone
from backend.models import HandoutModel
from django.core.urlresolvers import reverse
from django.http import JsonResponse
import datetime
import json
import ast
# handout_id = models.IntegerField(unique=True, null=True)
# teacher = models.CharField(max_length=128, null=True)
# period = models.IntegerField(null=True)
# file_name = models.CharField(max_length=128, null=True)
# due_date = models.DateTimeField(null=True)
# push_date = models.DateTimeField(null=True)
# google_identifier = models.CharField(max_length=128, null=True)
# invite_id = models.CharField(max_length=128, null=True)

class HandoutModelTestCase(TestCase):

	#using timezone to avoid runtime warning which complains about naive object not having timezone
    def setUp(self):
    	due_date = push_date = timezone.now()
        HandoutModel.objects.create(
            handout_id=11021994, teacher="Mr. Banks", period=4, file_name="testing",
            due_date=due_date, push_date=push_date, google_identifier="google", invite_id="id")

    def test_sanity_test(self):
        test_user = HandoutModel.objects.get(handout_id=11021994)
        self.assertEqual(test_user.teacher, "Mr. Banks")
        self.assertEqual(test_user.period, 4)
        self.assertEqual(test_user.file_name, "testing")
        self.assertEqual(test_user.due_date.day, timezone.now().day)
        self.assertEqual(test_user.push_date.day, timezone.now().day)


    def test_get_handouts(self):
        client = Client()
        response = client.get(
            '/get_handout/', {'teacher': 'Mr. Banks', 'period': 4}, content_type='application/json')
        print response.content
        value = dict(ast.literal_eval(response.content))
        self.assertEqual(value.get("file_name")[0], 'testing')
