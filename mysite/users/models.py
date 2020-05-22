# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    First_Name = models.CharField(max_length = 20)
    Last_Name = models.CharField(max_length = 20)
    Favorite_Sandwich = models.CharField(max_length = 20)
    Bio = models.CharField(max_length = 500)
