from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
