from django.db import models
from django.utils import timezone
import datetime
import StringIO
import logging
import ast
from django.db import IntegrityError

# field for having the model take in a list for processing
# Credits to jathanism on StackOverflow
# http://stackoverflow.com/questions/5216162/how-to-create-list-field-in-django


class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value
        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class UsersModel(models.Model):
    user = models.CharField(unique=True, max_length=128)
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    teacher = ListField(null=True)
    # teacher = models.CharField(max_length=128, null=True)
    school = models.CharField(max_length=128, null=True)
    period = ListField(null=True)
    email = models.CharField(max_length=128, unique=True, null=True)

    def login(self, username):
        try:
            selected_choice = UsersModel.objects.get(user=username)
        except UsersModel.DoesNotExist:
            errcode = -1
            return [None, errcode, None, None]
        else:
            errcode = 1
            return [selected_choice.user, errcode, selected_choice.teacher, selected_choice.period]

    # WARNING: We can take out this method. It can be deprecated
    def get_user_id(self, username):
        try:
            selected_choice = UsersModel.objects.get(user=username)
        except:
            errcode = -1
            return [None, errcode]
        else:
            errcode = 1
            return[selected_choice.user, errcode]

    def add_user(self, username, school, teacher, period, first_name, last_name, email):
        try:
            selected_choice = UsersModel.objects.get(user=username)
        except UsersModel.DoesNotExist:
            newuser = UsersModel()
            newuser.user = username
            newuser.teacher = teacher
            newuser.school = school
            newuser.period = period
            newuser.user_id = len(UsersModel.objects.all())
            newuser.first_name = first_name
            newuser.last_name = last_name
            newuser.email = email
            newuser.save()
            errcode = 1
            return [errcode, 0]
        else:
            # that user is already there
            errcode = -1
            return [errcode, 0]

    def get_classmates(self, t, p, u):
        try:
            selected_choice = []
            everything = UsersModel.objects.all()
            for choices in everything:
                if t in choices.teacher and int(p) in choices.period and u != choices.user:
                    selected_choice.append(choices)

        except UsersModel.DoesNotExist:
            return [None, None, None, -1]
        # WE NEED TO WAIT FOR THE QUERY TO RETURN!
        else:
            first_names = []
            last_names = []
            user_ids = []
            for x in selected_choice:
                first_names.append(x.first_name)
                last_names.append(x.last_name)
                user_ids.append(x.user)
            return [first_names, last_names, user_ids, 1]


class TeacherModel(models.Model):
    user_id = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    school = models.CharField(max_length=128, null=True)
    period = ListField(null=True)
    email = models.CharField(max_length=128, null=True)

    def login(self, username):
        try:
            selected_choice = TeacherModel.objects.get(user_id=username)
        except UsersModel.DoesNotExist:
            errcode = -1
            return [None, errcode, None, None]
        else:
            errcode = 1
            return [selected_choice.user_id, errcode, selected_choice.first_name, selected_choice.period]

    def get_teacher_id(self, username):
        try:
            selected_choice = TeacherModel.objects.get(user_id=username)
        except:
            errcode = -1
            return [None, errcode]
        else:
            errcode = 1
            return[selected_choice.user_id, errcode]

    def add_teacher(self, username, first_name, last_name, school, period, email):
        try:
            selected_choice = TeacherModel.objects.get(user_id=username)
        except UsersModel.DoesNotExist:
            newuser = UsersModel()
            newuser.user_id = username
            newuser.first_name = first_name
            newuser.last_name = last_name
            newuser.school = school
            newuser.period = period
            newuser.email = email
            newuser.save()
            errcode = 1
            return [errcode, 0]
        else:
            # that user is already there
            errcode = -1
            return [errcode, 0]


class InvitesModel(models.Model):
    # user = models.CharField(max_length=128, null=True)
    inviter = models.CharField(max_length=128, null=True)
    invite_id = models.CharField(max_length=128, null=True)
    handout_id = models.CharField(max_length=128, null=True)
    invite_date = models.DateTimeField(null=True)
    invitee = ListField(null=True)

    """
    This needs to be updated
    class Meta:
        unique_together = ("user_id", "handout")
    """

    def put_invite(self, h, inviter, invitee):
        newinvite = InvitesModel()
        newinvite.inviter = inviter
        newinvite.invitee = invitee
        newinvite.handout_id = h
        newinvite.invite_date = timezone.now()

        try:
            newinvite.save()
            return 1
        except IntegrityError:
            return -1

    # returns -1 if there are no items found, and 1 if items are found
    def get_invite(self, u):
        try:
            everything = InvitesModel.objects.all()
            file_names = []
            dates = []
            for choices in everything:
                if u in choices.invitee:
                    file_names.append(choices.handout_id)
                    dates.append(str(choices.invite_date))
            return [file_names, dates, 1]
        except InvitesModel.DoesNotExist:
            return [None, None, -1]


class HandoutModel(models.Model):
    # We aren't having teachers push out the files itself, once that happens
    # we will use a File ID
    handout_id = models.CharField(max_length=128, null=True)
    teacher = models.CharField(max_length=128, null=True)
    period = models.IntegerField(null=True)
    file_name = models.CharField(max_length=128, null=True)
    due_date = models.DateTimeField(null=True)
    push_date = models.DateTimeField(null=True)
    google_id = models.CharField(max_length=128, null=True)
    invite_id = models.CharField(max_length=128, null=True)

    """
    @returns a list of handout objects (up to 3)
    if there are no handouts, it will return a handout List with 1 item [None]
    """

    def get_handouts(self, teacher, period):
        try:
            selected_choice = HandoutModel.objects.filter(
                teacher=teacher, period=period).order_by('due_date')
        except HandoutModel.DoesNotExist:
            return None
        else:
            result = {'file_name': [], 'due_date': [], 'google_id': []}
            i = 0
            for x in selected_choice:
                result['file_name'].append(x.file_name)
                result['due_date'].append(str(x.due_date))
                result['google_id'].append(x.google_id)
                i += 1
                if i == 3:
                    break
            return result

    def put_handout(self, t, p, f):
        try:
            selected_choice = HandoutModel.objects.get(file_name=f)
        except HandoutModel.DoesNotExist:
            newhand = HandoutModel()
            newhand.handout_id = len(HandoutModel.objects.all())
            newhand.teacher = t
            newhand.period = p
            newhand.file_name = f
            newhand.due_date = datetime.datetime.now()
            newhand.save()
            errcode = 1
            return errcode
        else:
            # that handout is already there
            errcode = -1
            return errcode

    def get_handout_from_file_name(self, f):
        try:
            selected_choice = HandoutModel.objects.get(file_name=f)
        except HandoutModel.DoesNotExist:
            return None
        else:
            return selected_choice


class GTLFiles(models.Model):
    google_id = models.CharField(max_length=128, null=True)
    title = models.CharField(max_length=128, null=True)
    thumbnailLink = models.CharField(max_length=128, null=True)
