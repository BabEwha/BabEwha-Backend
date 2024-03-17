# users/models.py

from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from django.db import models
from .managers import UserManager

class User(AbstractBaseUser):
    class Meta :
        db_table = 'user'

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    @property
    def is_superuser(self):
        return self.is_staff

    @property
    def is_staff(self):
       return self.is_staff

    def has_perm(self, perm, obj=None):
       return self.is_staff

    def has_module_perms(self, app_label):
       return self.is_staff

    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[RegexValidator(
            regex='^[a-zA-Z0-9_.+-]+@ewhain.net$',
            message='Email must end with @ewhain.net',
            code='invalid_email'
        )]
    )
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

class Profile(models.Model):
    class Meta :
        db_table = 'profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=20)

    def __str__(self):
        return self.nickname
