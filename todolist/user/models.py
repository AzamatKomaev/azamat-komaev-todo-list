from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'User with given email already exists.'
        }
    )
    password = models.CharField(
        'password',
        max_length=128,
        validators=[RegexValidator(regex='^.{8,}$', message='Length hasnt to be less than 8', code='nomatch')])

