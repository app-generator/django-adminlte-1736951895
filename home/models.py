# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class User(models.Model):

    #__User_FIELDS__
    user_name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    other_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.BooleanField()
    residential_address = models.TextField(max_length=255, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Userprofile(models.Model):

    #__Userprofile_FIELDS__
    role_choices = models.BooleanField()
    address = models.TextField(max_length=255, null=True, blank=True)
    gender = models.BooleanField()
    phone = models.IntegerField(null=True, blank=True)
    matriculation_no = models.CharField(max_length=255, null=True, blank=True)
    school = models.ForeignKey(User, on_delete=models.CASCADE)

    #__Userprofile_FIELDS__END

    class Meta:
        verbose_name        = _("Userprofile")
        verbose_name_plural = _("Userprofile")



#__MODELS__END
