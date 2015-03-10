from django.test import TestCase
from backend.models import TeacherModel


class TeacherModelTestCase(TestCase):

    def setUp(self):
        TeacherModel.objects.create(user_id="t1", first_name="Marissa", last_name="Tomazoski",
                                    school="Wm Fremd High School", period=[6, 8],
                                    email="classboard.teacher2@gmail.com")

    def test_sanity(self):
    	test_teacher = TeacherModel.objects.get(user_id="t1")
    	self.assertEqual(test_teacher.period[0], 6)
    	self.assertEqual(test_teacher.period[1], 8)
