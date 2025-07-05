# users/models.py

from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    phone = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    address = models.TextField(blank=True)
    photo = models.ImageField(upload_to='user/profile/', blank=True, null=True)

    def __str__(self):
        return self.user.username
