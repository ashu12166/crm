from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# class Freelancer(models.Model):
#     firstname = models.CharField(max_length=20)
#     lastname = models.CharField(max_length=20)
#     interest = models.CharField(max_length=200)
#     skils = models.TextField()
#     experience = models.TextField()
#
#     def __str__(self):
#         return self.firstname

# class Clients(models.Model):
#     name = models.charfield(amx_length=20)
#     firm_name = models.charfield(max_length=20)
#     reference = models.charfield(max_length=200)
#     chu = models.charfield(max_length=200)