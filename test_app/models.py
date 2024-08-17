from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager
role_select=role_select = (
    ('SA', 'Super Admin'),
    ('AM', 'Admin')
)
class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    is_deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField('email address', unique = True)
    role = models.CharField(max_length=3, choices=role_select)
    groups = models.ManyToManyField(
    'auth.Group',
    related_name='custom_user_set',
    blank=True,
    )
    user_permissions = models.ManyToManyField(
    'auth.Permission',
    related_name='custom_user_permissions',
    blank=True,
    )
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
      return "{}".format(self.email)


