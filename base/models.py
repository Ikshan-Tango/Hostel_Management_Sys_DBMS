from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

from string import ascii_uppercase


from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)

    is_student   = models.BooleanField(default=False)
    is_caretaker   = models.BooleanField(default=False)
    is_warden   = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Student(models.Model):

    # blank_choice = [('', 'Choose'),]
    # hostels      = [("Hostel " + h, "Hostel " + h) for h in ascii_uppercase[:15]]

    student    = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    college_id = models.CharField(primary_key = True, max_length=20)
    name       = models.CharField(max_length=50)
    age        = models.PositiveIntegerField()
    # room_num   = models.CharField(max_length=10)
    # hostel     = models.CharField(max_length=10, choices=blank_choice + hostels)
    mobile_num = PhoneNumberField(null=False, blank=True, unique=True)
    branch      = models.CharField(max_length=20, null=True)
    year        = models.PositiveIntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.college_id} {self.name}"
    
class Caretaker(models.Model):
    
        caretaker  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        name       = models.CharField(max_length=50)
        age        = models.PositiveIntegerField()
        mobile_num = PhoneNumberField(null=False, blank=True, unique=True)
        # hostel     = models.CharField(max_length=10)
    
        def __str__(self) -> str:
            return f"{self.name}"
        
class Warden(models.Model):
     
    warden  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name       = models.CharField(max_length=50)
    age        = models.PositiveIntegerField()
    mobile_num = PhoneNumberField(null=False, blank=True, unique=True)
    # hostel     = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.name}"