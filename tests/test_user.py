from django.test import TestCase
from backend.models import UsersModel
import simplejson
import json

class UsersModelTestCase(TestCase):

    def setUp(self):
        UsersModel.objects.create(user="felixliu", first_name="felix", last_name="liu",
                                  teacher=["Mr. Banks"], school="Berkeley", period=[2],
                                  email="felixliu@berkeley.edu")

    def test_sanity_test(self):
        test_user = UsersModel.objects.get(user="felixliu")
        self.assertEqual(test_user.first_name, 'felix')
        self.assertEqual(test_user.teacher[0], "Mr. Banks")
        self.assertEqual(test_user.period[0], 2)
        json_file = open("backend/fixtures/populate.json")
        json_data = "".join(json_file.readlines())
        print json_data
        json.loads(json_data)

