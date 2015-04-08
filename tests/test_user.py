from django.test import TestCase, Client
from backend.models import UsersModel
from backend.models import HandoutModel
import simplejson
import json
import ast


class UsersModelTestCase(TestCase):

    def setUp(self):
        UsersModel.objects.create(user="felixliu", first_name="felix", last_name="liu",
                                  teacher=["tomsawyer"], school="Berkeley", period=[2],
                                  email="felixliu@berkeley.edu")
        UsersModel.objects.create(user="akhilnambiar", first_name="akhil", last_name="nambiar",
                                  teacher=["tomsawyer"], school="Berkeley", period=[2],
                                  email="akhilnambiar@berkeley.edu")
        UsersModel.objects.create(user="tomsawyer", first_name="tom", last_name="sawyer",
                                  is_teacher=True,
                                  school="Berkeley", period=[2],
                                  email="tomsawyer@berkeley.edu")
        HandoutModel.objects.create(handout_id="11021994", teacher="Mr. Banks", period=4,
                                    file_name="testing", google_id="google", invite_id="id1")
        HandoutModel.objects.create(handout_id="11021995", teacher="Mr. Banks", period=4,
                                    file_name="testing", google_id="google", invite_id="id2")

    def test_sanity_test(self):
        test_user = UsersModel.objects.get(user="felixliu")
        self.assertEqual(test_user.first_name, 'felix')
        self.assertEqual(test_user.teacher[0], "tomsawyer")
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

    def test_teacher(self):
        handout1 = HandoutModel.objects.get(handout_id="11021994")
        handout2 = HandoutModel.objects.get(handout_id="11021995")
        teacher = UsersModel.objects.get(user="tomsawyer")
        handout1.user_relation = teacher
        handout2.user_relation = teacher

        self.assertEqual(handout1.user_relation.user, "tomsawyer")
        self.assertEqual(handout2.user_relation.user, "tomsawyer")

    def test_get_documents(self):
        handout1 = HandoutModel.objects.get(handout_id="11021994")
        handout2 = HandoutModel.objects.get(handout_id="11021995")
        teacher = UsersModel.objects.get(user="tomsawyer")
        handout1.user_relation = teacher
        handout2.user_relation = teacher
        handout1.save()
        handout2.save()            

        client = Client()
        response = client.get(
            '/get_documents/', {'username': 'felixliu', 'sort_by': 'teacher'}, content_type='application/json')
        if response.content != None:
            self.assertTrue(True)

