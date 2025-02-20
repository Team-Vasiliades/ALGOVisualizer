from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db import models
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    profile_photo = models.BinaryField(blank=True, null=True)
    email= models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    institute = models.CharField(max_length=255, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

from django.contrib.auth.models import User

# Create your models here.

class HomeChatroom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Chatroom(models.Model):
    name = models.CharField(max_length=5000)
    
    def _str_(self):
        return self.name

class Chat(models.Model):
    chat_content = models.CharField(max_length=5000)
    user = models.CharField(max_length=5000)
    room = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)

    