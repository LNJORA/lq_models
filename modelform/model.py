from __future__ import unicode_literals
from django.db import models


class Register(models.Model):
    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER'),
    ]
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=20)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Date = models.DateField()
    Age = models.IntegerField()
    upload = models.ImageField()
# M-Male F-Female O-Other

class Meta:
    db_table = "student"
