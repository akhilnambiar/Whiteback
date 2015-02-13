from django.db import models
from django.db import IntegrityError

class User(models.Model):
    user = models.CharField(unique=True, max_length=128)
    test = models.CharField(unique=True, max_length=128)

    def login(self, username):
        # try:
        selected_choice = User.objects.get(user=username)
        return
        # except User.DoesNotExist:
        #   error_code = -1
        #   return []
        # finally:
        #   error_code = 1
        #   return "yes"

    def get_user_id(self, username):
        selected_choice = User.objects.get(user=username)
        return

    def add_user(self, username):
        new_user = User()
        new_user.user = username
        new_user.save()
        return
