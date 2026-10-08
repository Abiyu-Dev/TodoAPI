from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    class Meta:
        db_table = 'accounts_user'

    def __str__(self):
        return self.username


