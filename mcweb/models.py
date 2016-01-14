from django.db import models


class Merchant(models.Model):
    user = models.ForeignKey('auth.User')
    display_name = models.CharField(max_length=100, null=False, unique=True)
    redirect_url = models.URLField(max_length=100,null=True)
    address = models.CharField(max_length=500,null=True)


