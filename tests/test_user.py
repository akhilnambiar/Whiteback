from django.test import TestCase, Client
from backend.models import UsersModel
import simplejson
import json
import ast


class UsersModelTestCase(TestCase):

    def setUp(self):
        UsersModel.objects.create(user="felixliu", first_name="felix", last_name="liu",
                                  teacher=["Mr. Banks"], school="Berkeley", period=[2],
                                  email="felixliu@berkeley.edu")
        UsersModel.objects.create(user="akhilnambiar", first_name="akhil", last_name="nambiar",
                                  teacher=["Mr. Banks"], school="Berkeley", period=[2],
                                  email="akhilnambiar@berkeley.edu")
        UsersModel.objects.create(user="tomsawyer", first_name="tom", last_name="sawyer",
                                  teacher=["Mr. Banks"], school="Berkeley", period=[2],
                                  email="tomsawyer@berkeley.edu")

    def test_sanity_test(self):
        test_user = UsersModel.objects.get(user="felixliu")
        self.assertEqual(test_user.first_name, 'felix')
        self.assertEqual(test_user.teacher[0], "Mr. Banks")
        self.assertEqual(test_user.period[0], 2)
        json_file = open("backend/fixtures/populate.json")
        json_data = "".join(json_file.readlines())
        # print json_data
        json.loads(json_data)

    def test_get_classmates_test(self):
        client = Client()
        response = client.get(
            '/get_classmates/', {'teacher': ["Mr. Banks"], 'period': [2], 'user': 'felixliu'}, content_type='application/json')
        value = dict(ast.literal_eval(response.content))
        # print value
        self.assertEqual('felix', 'felix')
        









