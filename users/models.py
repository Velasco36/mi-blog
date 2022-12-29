from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User, PermissionsMixin, AbstractBaseUser
from django.conf import settings
from django.db.models.signals import post_save
from .managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    
    name= models.CharField(max_length=50, default='')
    username=models.CharField(max_length=50, default='')
    last_name= models.CharField(max_length=60, default='')
    password=models.CharField(max_length=60, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_init = models.DateField(
        'Fecha inicio', blank=True, null=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()