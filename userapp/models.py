from django.contrib.auth.models import User, AbstractUser
from django.db import models

from userapp.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('Email', unique=True, db_index=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'