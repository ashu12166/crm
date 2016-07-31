from django.contrib.auth.tests.custom_user import CustomUserManager
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,User
from crm import settings


class FreelancerManager(BaseUserManager):
    def create_user(self, email, skills, field_of_interest, experience, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            skills=skills,
            field_of_interest=field_of_interest,
            experience=experience,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, field_of_interest, experience, skills, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            skills=skills,
            field_of_interest=field_of_interest,
            experience=experience,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Freelancer(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    field_of_interest = models.CharField(max_length=200)
    skills = models.TextField()
    experience = models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = FreelancerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['skills', 'field_of_interest', 'experience']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Clients(models.Model):
    name = models.CharField(max_length=20)
    firm_name = models.CharField(max_length=20)
    reference = models.CharField(max_length=200)
    chu = models.CharField(max_length=200)

    def __str__(self):
        return self.name
