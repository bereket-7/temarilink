from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from apps.common.models import BaseModel
from apps.schools.models import School

class UserManager(BaseUserManager):
    def create_user(self, phone, full_name, role, password=None, school=None):
        if not phone:
            raise ValueError('Users must have a phone number')
        user = self.model(
            phone=phone,
            full_name=full_name,
            role=role,
            school=school
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, full_name, role='ADMIN', password=None, school=None):
        user = self.create_user(
            phone=phone,
            full_name=full_name,
            role=role,
            password=password,
            school=school
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    ADMIN = 'ADMIN'
    TEACHER = 'TEACHER'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (TEACHER, 'Teacher'),
    ]

    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return f"{self.full_name} ({self.role})"
