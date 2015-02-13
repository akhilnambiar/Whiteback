from django.db import models
from django.db import IntegrityError

class User(models.Model):
    user = models.CharField(unique=True,max_length=128)

    def login(self, username):
    	# try:
		selected_choice = User.objects.get(user=username)
		# except User.DoesNotExist:
		# 	error_code = -1
		# 	return []
		# finally:
		# 	error_code = 1
		# 	return "yes"
