from django.test import TestCase, Client
from backend.models import HandoutModel
from django.core.urlresolvers import reverse
import json
import ast
from django.http import JsonResponse
# import urllib.parse
# handout_id = models.IntegerField(unique=True, null=True)
# teacher = models.CharField(max_length=128, null=True)
# period = models.IntegerField(null=True)
# file_name = models.CharField(max_length=128, null=True)
# date = models.DateTimeField(null=True)


class HandoutModelTestCase(TestCase):

    def setUp(self):
        HandoutModel.objects.create(
            handout_id=11021994, teacher="Mr. Banks", period=4, file_name="testing")

    def test_sanity_test(self):
        test_user = HandoutModel.objects.get(teacher="Mr. Banks")
        self.assertEqual(test_user.period, 4)

    def test_get_handouts(self):
    	client = Client()
    	# data = json.dumps({'teacher':'Mr. Banks', 'period':4})
    	# encdata = urllib.parse.urlencode(data)
    	response = client.get('/get_handout/', {'teacher':'Mr. Banks', 'period':4}, content_type='application/json')
    	value = dict(ast.literal_eval(response.content))
    	self.assertEqual(value.get("file_name")[0], 'testing')
