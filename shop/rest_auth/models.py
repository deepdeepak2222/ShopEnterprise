from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.


class AdminUser(AbstractUser):
    phone = models.CharField(max_length=15, null=False, blank=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class TokenModel(Token):
    """Token model"""
    pass
