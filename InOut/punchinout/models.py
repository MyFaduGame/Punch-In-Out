from enum import unique
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    userid = models.CharField(_("Userid"), max_length=50)
    firstname = models.CharField(_("Firstname"), max_length=50)
    lastname = models.CharField(_("Lastname"), max_length=50)
    phone_number = PhoneNumberField(unique=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['firstname', 'lastname','username']

    def __str__(self):
        return f"{self.userid}"

class timein(models.Model):
    userid = models.CharField(_("Userid"), max_length=50)
    dateuser = models.DateField(_("date"), auto_now=False, auto_now_add=True)
    timestampin = models.TimeField(_("Timeofentry"), auto_now=False, auto_now_add=True)

    REQUIRED_FIELDS = ['userid','dateuser','timestampin']    

    def __str__(self):
        return f"{self.userid}"

class timeout(models.Model):
    userid = models.CharField(_("Userid"), max_length=50, null=True)
    dateuser = models.DateField(_("Date"), auto_now=False, auto_now_add=True)
    timestampout = models.TimeField(_("Timeofout"), auto_now=False, auto_now_add=True)
