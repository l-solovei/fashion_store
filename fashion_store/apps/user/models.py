from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,
                                        PermissionsMixin)

from utils.abstract_models import CreateUpdateModel


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have an email')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)


class UserModel(AbstractBaseUser, PermissionsMixin, CreateUpdateModel):
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.EmailField(max_length=100, unique=True,
                              verbose_name='Email')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip = models.CharField(max_length=10, verbose_name='Zip')

    is_staff = models.BooleanField(default=False, verbose_name='Is Staff')
    is_superuser = models.BooleanField(default=False,
                                       verbose_name='Is Superuser')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
