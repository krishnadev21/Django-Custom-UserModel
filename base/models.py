from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, help_text='Name', null=True)
    email = models.EmailField(unique=True, help_text='Email')
    avatar = models.ImageField(null=True, default='avatar.svg')
    bio = models.TextField(max_length=500, help_text='Bio', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
