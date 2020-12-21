from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, unique=True, null=False)
    password = models.CharField(max_length=200, null=False)
