from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager():
    """Manager for user profile"""

    def create_user(self, email, name, password = None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password)
        user.save(using = self.db)

        return User


    def create_superuser(self, email, name, passward):
        """Create and save a new superuser with given details"""
        user = delf.create_user(email, name, passward)


        user.is_superuser = True
        user.is_staff = True
        user.save(using = self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in system"""

    email = models.EmailField(max_length=250, unique = True)
    name = models.CharField(max_length = 250)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['name']

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name


    def get_short_name(self):
        """Retrive short name of user"""
        return self.name


    def __str__(self):
        """Return string representation of our user"""
        return self.email
