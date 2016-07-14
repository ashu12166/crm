from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Freelancer(models.Model):
    name = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    field_of_interest = models.CharField(max_length=200)
    skills = models.TextField()
    experience = models.TextField()

    def __str__(self):
        return self.name


# class Clients(models.Model):
#     name = models.CharField(max_length=20)
#     firm_name = models.CharField(max_length=20)
#     reference = models.CharField(max_length=200)
#     chu = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name

