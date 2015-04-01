from django.test import TestCase, Client
from backend.models import InvitesModel
from django.http import JsonResponse
from django.utils import timezone
import simplejson
import json
import ast


class InvitesModelTestCase(TestCase):

    def setUp(self):
        invite_date = timezone.now()
        InvitesModel.objects.create(invite_id="i0", handout_id="h0",
                                    inviter="akhil", invitee=["felix"],
                                    invite_date=invite_date)
        InvitesModel.objects.create(invite_id="i0", handout_id="h1",
                                    inviter="akhil", invitee=["felix"],
                                    invite_date=invite_date)
        InvitesModel.objects.create(invite_id="i0", handout_id="h2",
                                    inviter="akhil", invitee=["felix"],
                                    invite_date=invite_date)

    def test_get_invites(self):
        client = Client()
        response = client.get(
            '/get_invites/', {'inviter': 'felix'}, content_type='application/json')
        value = dict(ast.literal_eval(response.content))
        # print value

    def test_send_invites(self):
        client = Client()
        response = client.post(
            '/send_invites/', {"inviter": "felix", "invitee": ["akhil", "ciara", "rain"]}, content_type='application/json')
        value = dict(ast.literal_eval(response.content))
        self.assertEqual(value.get('errcode'), 1)
        response = client.post(
            '/send_invites/', {'inviter': 'felix',
                               'invitee': ['akhil', 'ciara', 'rain'],
                               'file_name': 'hobos'}, content_type='application/json')
        value = dict(ast.literal_eval(response.content))
        self.assertEqual(value.get('errcode'), -2)
