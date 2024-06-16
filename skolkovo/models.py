import datetime

from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    creation_date = models.DateField()
    inn = models.CharField(max_length=10)


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    price = models.FloatField()
