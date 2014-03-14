from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser) :
# Fields of AbstractUser :
# -----
# 	username
# Required. 30 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.
# -----
# first_name
# Optional. 30 characters or fewer.
# -----
# last_name
# Optional. 30 characters or fewer.
# -----
# email
# Optional. Email address.
# -----
# password
# Required. A hash of, and metadata about, the password. (Django does not store the raw password.) Raw passwords can be arbitrarily long and can contain any character. See the password documentation.
# -----
# groups
# Many-to-many relationship to Group
# -----
# user_permissions
# Many-to-many relationship to Permission
# -----
# is_staff
# Boolean. Designates whether this user can access the admin site.
# -----
# is_active
# Boolean. Designates whether this user account should be considered active. We recommend that you set this flag to False instead of deleting accounts; that way, if your applications have any foreign keys to users, the foreign keys won't break.
# -----
# is_superuser
# Boolean. Designates that this user has all permissions without explicitly assigning them.
# -----
# last_login
# A datetime of the user's last login. Is set to the current date/time by default.
# -----
# date_joined
# A datetime designating when the account was created. Is set to the current date/time by default when the account is created.
# -----

		def __unicode__(self):
			return self.name