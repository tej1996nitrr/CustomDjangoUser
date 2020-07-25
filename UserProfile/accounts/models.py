from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from django.conf import settings


class CustomUser(AbstractUser):

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=10)
    bio = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email
