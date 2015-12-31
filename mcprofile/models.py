from __future__ import unicode_literals

from django.db import models


class Merchant(models.Model):
    display_name = models.CharField(max_length=100)

